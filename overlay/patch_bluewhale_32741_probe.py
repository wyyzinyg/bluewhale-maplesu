"""32741 (3.22.2-bw): probe queue deadlock fix + version bump.

Bug (seen on device 2026-11-28): the home root probe timed out once
("未检测到可用的 root 环境 / 探测超时了") and every later "重新检测" also failed,
because EnvironmentProbeRunner kept its single-flight lock held by a worker thread
that never exits after FutureTask.cancel(true) (a blocked su / readLine call does not
answer interrupts). Only a process restart cleared it.

Fix: replace the AtomicBoolean gate with an AtomicReference<Thread?> gate that is
released in the finally block of the caller as well, so a timed-out round can be
retried immediately while the stale daemon worker keeps its own exit path without
clearing the lock of a newer round.

Also bumps 32740/3.22.1-bw -> 32741/3.22.2-bw.
"""

from pathlib import Path

VERSION_CODE = "32741"
VERSION_NAME = "3.22.2-bw"

OLD_CLASS_MARKER = "class EnvironmentProbeRunner"

NEW_CLASS = '''class EnvironmentProbeRunner(private val threadName: String = "maplesu-environment-probe") {
    private val active = AtomicReference<Thread?>(null)

    suspend fun <T> run(timeoutMillis: Long, probe: () -> T): EnvironmentProbeResult<T> =
        withContext(Dispatchers.IO) {
            val task = FutureTask(Callable(probe))
            val worker = Thread({
                try { task.run() } finally { active.compareAndSet(Thread.currentThread(), null) }
            }, threadName).apply { isDaemon = true }
            if (!active.compareAndSet(null, worker)) return@withContext EnvironmentProbeResult.Busy
            worker.start()
            try {
                runInterruptible {
                    // Unwrap before a coroutine boundary can recover/copy ExecutionException.
                    try {
                        EnvironmentProbeResult.Completed(task.get(timeoutMillis.coerceAtLeast(1), TimeUnit.MILLISECONDS))
                    } catch (_: TimeoutException) {
                        EnvironmentProbeResult.TimedOut
                    } catch (error: ExecutionException) {
                        val cause = error.cause ?: error
                        if (cause is CancellationException) throw cause
                        EnvironmentProbeResult.Failed(cause)
                    }
                }
            } catch (cancelled: CancellationException) {
                throw cancelled
            } catch (error: Exception) {
                EnvironmentProbeResult.Failed(error)
            } finally {
                task.cancel(true)
                // 超时/取消后主动放锁：被中断也不退出的 native 调用不再永久占住探测队列，
                // 用户点「重新检测」可以立刻重新发起一轮；旧 worker 退出时按自身引用 CAS，
                // 不会误清新一轮持有的锁。
                active.compareAndSet(worker, null)
            }
        }
}
'''


def _bump_version(root: Path) -> None:
    gradle = root / "manager/build.gradle.kts"
    if not gradle.is_file():
        print("skip: manager/build.gradle.kts missing")
        return
    text = gradle.read_text(encoding="utf-8")
    changed = False
    for old, new in (("versionCode = 32740", f"versionCode = {VERSION_CODE}"),
                     ('versionName = "3.22.1-bw"', f'versionName = "{VERSION_NAME}"')):
        if old in text:
            text = text.replace(old, new, 1)
            changed = True
    if changed:
        gradle.write_text(text, encoding="utf-8")
        print(f"bumped manager version -> {VERSION_CODE}/{VERSION_NAME}")
    else:
        print("skip: version already bumped")


def _fix_probe_runner(root: Path) -> None:
    path = root / "manager/src/main/java/dev/maplesu/manager/workmode/EnvironmentProbeDeadline.kt"
    if not path.is_file():
        print("skip: EnvironmentProbeDeadline.kt missing")
        return
    text = path.read_text(encoding="utf-8")
    if "AtomicReference<Thread?>" in text:
        print("skip: probe runner already patched")
        return

    if "import java.util.concurrent.atomic.AtomicBoolean\n" in text:
        text = text.replace(
            "import java.util.concurrent.atomic.AtomicBoolean\n",
            "import java.util.concurrent.atomic.AtomicBoolean\n"
            "import java.util.concurrent.atomic.AtomicReference\n",
            1,
        )
    elif "import java.util.concurrent.atomic.AtomicReference\n" not in text:
        anchor = "import java.util.concurrent.TimeoutException\n"
        if anchor in text:
            text = text.replace(anchor, anchor + "import java.util.concurrent.atomic.AtomicReference\n", 1)
        else:
            lines = text.split("\n")
            idx = max((i for i, l in enumerate(lines) if l.startswith("import java.")), default=0)
            lines.insert(idx + 1, "import java.util.concurrent.atomic.AtomicReference")
            text = "\n".join(lines)

    idx = text.find(OLD_CLASS_MARKER)
    if idx < 0:
        raise SystemExit("FATAL: EnvironmentProbeRunner class not found")
    text = text[:idx] + NEW_CLASS
    path.write_text(text, encoding="utf-8")
    print("patched EnvironmentProbeDeadline.kt: retryable probe queue")


def patch_32741_probe(root: Path) -> None:
    _fix_probe_runner(root)
    _bump_version(root)


if __name__ == "__main__":
    import sys

    patch_32741_probe(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())

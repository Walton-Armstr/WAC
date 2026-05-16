import os
import sys


def configure_stdio_encoding():
    for stream_name in ("stdin", "stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None:
            continue

        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue

        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (OSError, ValueError):
            pass


def _stream_is_missing(stream):
    if stream is None:
        return True

    try:
        stream.fileno()
    except (AttributeError, OSError, ValueError):
        return True

    return False


def ensure_console():
    """Make stdio available for frozen/windowed Windows builds."""
    if os.name != "nt":
        return

    if not (
        _stream_is_missing(sys.stdin)
        or _stream_is_missing(sys.stdout)
        or _stream_is_missing(sys.stderr)
    ):
        return

    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        attach_parent_process = ctypes.c_uint(-1).value
        error_access_denied = 5

        if not kernel32.AttachConsole(attach_parent_process):
            if kernel32.GetLastError() != error_access_denied:
                kernel32.AllocConsole()

        sys.stdin = open("CONIN$", "r", encoding="utf-8", errors="replace")
        sys.stdout = open(
            "CONOUT$", "w", encoding="utf-8", errors="replace", buffering=1
        )
        sys.stderr = open(
            "CONOUT$", "w", encoding="utf-8", errors="replace", buffering=1
        )
        configure_stdio_encoding()

        try:
            from colorama import just_fix_windows_console

            just_fix_windows_console()
        except Exception:
            pass
    except OSError:
        return

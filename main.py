"""Business Automation Pro - entry point.

    python main.py                          # open the desktop application
    python main.py data.xlsx --all          # headless: report + invoices + export
    python main.py --sample --report        # try it with the bundled sample data
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    from app.cli import run_cli, wants_cli

    if wants_cli(argv):
        return run_cli(argv)

    try:
        from app.gui import run_gui
    except ImportError as exc:  # tkinter missing (common on minimal Linux installs)
        print(f"The desktop interface needs Tkinter ({exc}).")
        print("Install it (Debian/Ubuntu: sudo apt install python3-tk) or use the command line:")
        print("    python main.py --sample --all")
        return 1
    run_gui()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""
Reposting CLI — entry point.

This module is a placeholder for Phase 1.
Full subcommands (add, queue, run, history) are implemented in Phase 7.
"""

import argparse

from reposting import __version__


def main() -> None:
    """Parse arguments and dispatch to the appropriate subcommand."""
    parser = argparse.ArgumentParser(
        prog="reposting",
        description="Reposting — A modular content reposting automation toolkit.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"reposting {__version__}",
    )

    # Subcommands will be registered here in Phase 7.
    parser.add_argument(
        "command",
        nargs="?",
        help="Subcommand to run (coming in Phase 7).",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        print(f"🚧 Subcommand '{args.command}' is not yet implemented.")


if __name__ == "__main__":
    main()

"""
Reposting - A modular content reposting automation toolkit.

Entry point shim — delegates to the CLI package.
Run directly:  python main.py
Run as module: python -m reposting
"""

from reposting.cli.commands import main

if __name__ == "__main__":
    main()

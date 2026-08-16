#!/usr/bin/env python3
"""SessionStart hook: turn efficient-clear on by default for every new session."""
import os

FLAG_PATH = os.path.join(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude"), ".efficient-clear-active")

try:
    with open(FLAG_PATH, "w") as f:
        f.write("on")
    os.chmod(FLAG_PATH, 0o600)
except OSError:
    pass

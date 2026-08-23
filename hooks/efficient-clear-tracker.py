#!/usr/bin/env python3
"""UserPromptSubmit hook: toggle efficient-clear via chat phrases, and
re-inject a short reminder every turn while it's active — mirrors the
per-turn reinforcement pattern used by the caveman plugin's tracker hook."""
import json
import os
import re
import sys

CLAUDE_DIR = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
FLAG_PATH = os.path.join(CLAUDE_DIR, ".efficient-clear-active")
MAX_FLAG_BYTES = 32

ON_RE = re.compile(r"\b(activate|enable|turn on|start)\b.*\befficient[- ]?clear\b|\befficient[- ]?clear\b.*\b(mode|activate|enable|turn on|start)\b", re.I)
OFF_RE = re.compile(r"\b(stop|disable|deactivate|turn off)\b.*\befficient[- ]?clear\b|\befficient[- ]?clear\b.*\b(stop|disable|deactivate|turn off)\b", re.I)


def read_flag(path):
    try:
        if os.path.islink(path):
            return None
        st = os.stat(path)
        if st.st_size > MAX_FLAG_BYTES:
            return None
        with open(path) as f:
            return f.read(MAX_FLAG_BYTES).strip()
    except OSError:
        return None


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    prompt = (data.get("prompt") or "").strip()

    if OFF_RE.search(prompt):
        try:
            os.remove(FLAG_PATH)
        except OSError:
            pass
        return

    if ON_RE.search(prompt):
        try:
            with open(FLAG_PATH, "w") as f:
                f.write("on")
            os.chmod(FLAG_PATH, 0o600)
        except OSError:
            pass

    if read_flag(FLAG_PATH):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    "EFFICIENT-CLEAR MODE ACTIVE. "
                    "Cut filler, pleasantries, hedging, throat-clearing."
                    "Use general English, avoid analogies, jargon or niche expressions. "
                    "Be succint but don't trade clarity for brevity. "
                    "One word per meaning. Short word over long synonym."
                    "Active voice. "
                    "Internal reasoning is not visible to the reader — don't assume a "
                    "term or conclusion from it is already known; restate what the reader needs."
                    "Applies to all prose, chat, docs, "
                    "commits, PRs, comments. Not to code, identifiers, or creative writing."
                )
            }
        }))


if __name__ == "__main__":
    main()

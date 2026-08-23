# Standing-mode setup

`efficient-clear` can run two ways: loaded on demand through the Skill
tool (gets the full `SKILL.md`, including the word-cutting checklist), or
as a standing hook that injects a short reminder every turn without
loading the file at all. This project uses the second approach, the same
pattern the `caveman` plugin uses for its own always-on mode.

## What the hook actually injects

Not the full `SKILL.md`. A single hand-written line, about 65 words:

```
EFFICIENT-CLEAR MODE ACTIVE. Cut filler, pleasantries, hedging, throat-clearing.
Avoid analogies. Use general English, avoid niche expressions. Don't trade
clarity for brevity. One word per meaning. Short word over long synonym.
Active voice. Internal reasoning is not visible to the reader — don't assume
a term or conclusion from it is already known; restate what the reader needs.
Applies to all prose, chat, docs, commits, PRs, comments. Not to code,
identifiers, or creative writing.
```

This line lives in [`hooks/efficient-clear-tracker.py`](hooks/efficient-clear-tracker.py),
not in the skill file. Editing the skill file does not change what the hook
sends — the two are separate copies that can drift out of sync.

## The two scripts

- [`hooks/efficient-clear-activate.py`](hooks/efficient-clear-activate.py) —
  runs on `SessionStart`. Writes a flag file (`~/.claude/.efficient-clear-active`)
  so the mode is on by default in every new session, with no trigger phrase
  needed.
- [`hooks/efficient-clear-tracker.py`](hooks/efficient-clear-tracker.py) —
  runs on `UserPromptSubmit`, every turn. Checks the flag file, and:
  - if a message contains an activation phrase ("activate efficient-clear",
    "turn on efficient-clear", …), writes the flag on.
  - if a message contains a deactivation phrase ("stop efficient-clear",
    "turn off efficient-clear", …), deletes the flag file.
  - if the flag file is present, prints the reminder line above as
    `additionalContext` for that turn.

## Wiring (in `~/.claude/settings.json`)

```json
"hooks": {
  "SessionStart": [
    { "matcher": "", "hooks": [
      { "type": "command", "command": "python3 \"/Users/xbits/.claude/hooks/efficient-clear-activate.py\"", "timeout": 5 }
    ]}
  ],
  "UserPromptSubmit": [
    { "matcher": "", "hooks": [
      { "type": "command", "command": "python3 \"/Users/xbits/.claude/hooks/efficient-clear-tracker.py\"", "timeout": 5 }
    ]}
  ]
}
```

## Cost and scope

- The reminder runs every turn, roughly 70 tokens each time. On a 50-turn
  session that is about 3,500 tokens. It re-injects because a style
  instruction given once tends to lose priority against other context
  later in a session — the same reasoning the `caveman` plugin's own hook
  comments give for its per-turn reinforcement.
- The reminder fires once per turn, before any output for that turn is
  generated — including reasoning — so it is in context for both. It is
  not scoped to final text only.
- The carve-out ("not to code, identifiers, or creative writing") is
  deliberately narrow: commit messages, PR descriptions, and comments are
  in scope. Code and creative writing are not.

## Known gap

The hook line and the `SKILL.md` file are maintained separately, by hand.
[`tests/a-star/efficient-clear-hookline.md`](tests/a-star/efficient-clear-hookline.md)
tests the hook line alone, with the Skill tool never invoked, against
[`tests/a-star/efficient-clear.md`](tests/a-star/efficient-clear.md), which
used the full skill file. Word counts came out close (508 vs. 521) on that
one test, but that is not a guarantee the two always agree — a future edit
to one and not the other goes unnoticed without a test like this.

This already happened once: a no-analogies rule was added to the hook line
directly, without a matching edit to `SKILL.md` — caught only when asked
which file governs actual behavior. Both files now carry the no-analogies
rule and a rule against assuming the reader can see internal reasoning, but
nothing enforces that they stay matched. Whoever edits one should edit the
other in the same change.

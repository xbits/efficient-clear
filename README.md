# efficient-clear

Three writing-style skills for Claude Code, plus a comparison test against two
external skills (caveman compression and Simplified Technical English).

## Skills in this repo

- [`skills/efficient-clear`](skills/efficient-clear/SKILL.md) — terse, dense,
  fully readable. Drops words that don't add readability, picks short words
  over long synonyms, uses one word per meaning. Self-contained, no
  dependency on the other skills below.
- [`skills/plain-speak`](skills/plain-speak/SKILL.md) — plain, universal
  English for any competent reader. No filler, no jargon, no needless
  analogies.
- [`skills/plain-speak-joao`](skills/plain-speak-joao/SKILL.md) — same goal,
  tuned for a specific reader profile: fluent non-native English speaker,
  software engineer, no formal academic background, no region-specific
  idioms.

## Test: A* pathfinding, five ways

Each skill (plus two external ones, for comparison) was given the same bare
prompt — "describe the A* pathfinding algorithm" — with no other framing, by
a separate agent that loaded only that one skill. Outputs are in
[`tests/a-star/`](tests/a-star/).

| Skill | Words | Notes |
|---|---:|---|
| `caveman.txt` | 252 | Symbol-heavy, sentence fragments, math notation as shorthand. Fastest read for someone who already knows the domain, hardest for a newcomer. |
| `unslop-text.txt` | 494 | Full sentences throughout, no markdown headers or bold. Defines admissible/consistent explicitly. Closest to a textbook paragraph. |
| `efficient-clear.txt` | 521 | Markdown headers and bold labels, denser than unslop-text per sentence. Only one to mention IDA*/SMA* memory-bounded variants. |
| `plain-speak.txt` | 634 | Longest. Most explanatory tone, restates ideas from a second angle ("moves close to a straight line toward the goal"). |
| `plain-speak-joao.txt` | 447 | Markdown headers, bold labels, no restating. Shortest of the header-formatted outputs. |

Raw word counts:

```
252 caveman.txt
447 plain-speak-joao.txt
494 unslop-text.txt
521 efficient-clear.txt
634 plain-speak.txt
```

## Method

- One fresh agent per skill, no shared context between them.
- Each agent was told which skill to load and given the task — nothing about
  the fact that outputs would be compared, and no style instructions beyond
  "load this skill."
- caveman and Simplified Technical English (STE) are external skills, not
  reproduced in this repo. Their SKILL.md sources are not ours to
  redistribute; only their test output is included, for comparison.

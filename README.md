# efficient-clear

Three writing-style skills for Claude Code, plus a comparison test against
three external skills: caveman compression, and two Simplified Technical
English variants.

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
- [`skills/unslop-text-ste.md`](skills/unslop-text-ste.md/SKILL.md) —
  Simplified Technical English variant, bundled with the `anthropic-skills`
  plugin.
- [`skills/ste-writing`](skills/ste-writing/SKILL.md) — Simplified Technical
  English variant against the full ASD-STE100 spec (Issue 9), with write /
  rewrite / review modes and an optional lint script. Source:
  [woosal1337/blog](https://github.com/woosal1337/blog/blob/main/videos/ep01-the-cure-for-ai-slop/ste-writing-skill.md).

## Test: A* pathfinding, six ways

Each skill (plus one external one, caveman, for comparison) was given the
same bare prompt — "describe the A* pathfinding algorithm" — with no other
framing, by a separate agent that loaded only that one skill. Outputs are in
[`tests/a-star/`](tests/a-star/).

| Skill | Words | Notes |
|---|---:|---|
| `caveman.md` | 252 | Symbol-heavy, sentence fragments, math notation as shorthand. Fastest read for someone who already knows the domain, hardest for a newcomer. |
| `ste-writing.md` | 480 | Full sentences, no markdown headers or bold, no contractions. Closest fit to the ASD-STE100 spec: short paragraphs, one topic each, plain connectors. |
| `unslop-text.md` | 494 | Full sentences throughout, no markdown headers or bold. Defines admissible/consistent explicitly. Closest to a textbook paragraph. |
| `efficient-clear.md` | 521 | Markdown headers and bold labels, denser than unslop-text per sentence. Only one to mention IDA*/SMA* memory-bounded variants. |
| `plain-speak-joao.md` | 447 | Markdown headers, bold labels, no restating. Shortest of the header-formatted outputs. |
| `plain-speak.md` | 634 | Longest. Most explanatory tone, restates ideas from a second angle ("moves close to a straight line toward the goal"). |
| `efficient-clear-hookline.md` | 508 | Same task, but with only the ~55-word hook reminder as the style instruction — no Skill tool call, no access to the full `efficient-clear` SKILL.md. See note below. |

Raw word counts:

```
252 caveman.md
447 plain-speak-joao.md
480 ste-writing.md
494 unslop-text.md
508 efficient-clear-hookline.md
521 efficient-clear.md
634 plain-speak.md
```

### Full skill vs. hook-line-only

`efficient-clear` runs in this project as a standing hook: every turn, a
short instruction (not the full `SKILL.md`) gets injected into context —
see [`hooks-setup.md`](hooks-setup.md). `efficient-clear-hookline.md` tests
that short line alone, with the Skill tool never invoked. Result: 508 words
against 521 for the full skill, and the same structure (headers, bold
labels, key-properties list). The short line carries most of the effect on
its own; the full skill adds the word-cutting checklist and the explicit
keep-list (articles, connectors) but the output difference here is small.

`unslop-text.md` and `ste-writing.md` come from two different Simplified
Technical English skills (different sources, same underlying ASD-STE100
rule set), and land within 14 words of each other. `efficient-clear.md`
targets the same readability goal without the STE word-list restriction,
and comes out close in length but with more structure (headers, bold).

## Method

- One fresh agent per skill, no shared context between them.
- Each agent was told which skill to load and given the task — nothing about
  the fact that outputs would be compared, and no style instructions beyond
  "load this skill."
- caveman is an external skill, not reproduced in this repo. Its SKILL.md
  source is not ours to redistribute; only its test output is included, for
  comparison.

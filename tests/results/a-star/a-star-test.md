
## Skills tested

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
- [`tests/alternative-skills/unslop-cursor`](../../alternative-skills/unslop-cursor/SKILL.md) —
  "cut AI tells from any writing" skill: a pattern list of AI writing tics
  (puffery, hedging, em-dash overuse, inline-header lists, and more) plus a
  self-audit step, rather than a positive style guide. Source:
  [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md).
- [`tests/alternative-skills/eff-clear-plus-unslop`](../../alternative-skills/eff-clear-plus-unslop/SKILL.md) —
  new skill written after testing `unslop-cursor`, folding some of its rules
  (abstract-metaphor-noun list, em-dash ban) into the `efficient-clear`
  structure (goals, directives, word-cutting rule, pre-send checklist).

## Test: A* pathfinding, eight ways

Each skill (plus one external one, caveman, for comparison) was given the
same bare prompt — "describe the A* pathfinding algorithm" — with no other
framing, by a separate agent that loaded only that one skill. Outputs are in
[`tests/a-star/`](tests/a-star/).

| Skill | Words | Notes |
|---|---:|---|
| `eff-clear-plus-unslop.md` | 301 | Full prose plus a numbered step list and a three-item definition list for g/h/f — the only entry to lay out the algorithm as literal steps rather than describing it in paragraphs. Shortest full-sentence output. |
| `unslop-cursor.md` | 314 | Full prose, no headers or bold. No formula-as-notation restraint — still writes out f(n) = g(n) + h(n), but skips restating properties in list form. |
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
301 eff-clear-plus-unslop.md
314 unslop-cursor.md
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

### eff-clear-plus-unslop

Shortest full-prose result, and the only one that renders the algorithm as
a numbered step list instead of describing it in paragraphs — the format
itself removes words a paragraph would need for transitions ("next",
"then the algorithm checks whether"). It also skips the properties section
(admissible, consistent, optimal) that `efficient-clear.md` and
`unslop-text.md` both include, folding the one property that matters
(heuristic must not overestimate) into a single sentence instead.

### unslop-cursor is an edit skill, not a write skill

Its description is "Cut AI tells from any writing" and its process is
scan-then-rewrite against a pattern list (puffery, hedging, em dashes,
inline-header lists, and more), plus a "what makes this obviously AI
generated?" self-audit — not a positive style guide like the others tested
here. Given the same bare prompt with no draft to edit, the agent wrote a
draft and then applied the skill's checklist to it. The result is the
shortest full-prose output in this test, with no headers or bold, which
matches the skill's explicit rule against inline-header lists ("bold label
and colon that restates the line").

## Method

- One fresh agent per skill, no shared context between them.
- Each agent was told which skill to load and given the task — nothing about
  the fact that outputs would be compared, and no style instructions beyond
  "load this skill."
- caveman is an external skill, not reproduced in this repo. Its SKILL.md
  source is not ours to redistribute; only its test output is included, for
  comparison.
- The `efficient-clear` standing hook (see [`hooks-setup.md`](../../../hooks-setup.md))
  injects a style reminder on every `UserPromptSubmit` in this user's Claude
  Code setup. That hook fires only on the main session's prompt submission,
  not on Task-tool subagent calls, so it should not reach an agent spawned
  through the Agent tool. As a precaution for the `unslop-cursor` run, the
  hook's activation flag (`~/.claude/.efficient-clear-active`) was removed
  before spawning the agent and restored after, so the test ran with the
  injection mechanism fully off rather than relying on that assumption.

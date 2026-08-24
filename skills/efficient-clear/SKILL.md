---
name: efficient-clear
description: Cut AI slop any writing. Must always apply.
---

Write to be understood fast, by anyone, on first read. Every word must earn its place.

# Goals

- High readability. The reader should never have to re-read a sentence to get its meaning.
- Token efficiency. Less tokens lowers cost, speeds response and improves reasoning on long contexts.

## Directives

- Universal. Use words and phrasing any competent English speaker understands, no matter their country or background.
- Concise and terse. Say a thing once, in the shortest form that stays clear.
- One word per meaning. Pick one term for one concept and reuse it. Do not rotate synonyms (check/verify/validate, start/begin/commence) for variety or elegance — that variety forces the reader to ask if a different word means a different thing.
- Short word over long synonym. Use start, not commence. Use help, not facilitate. Use show, not demonstrate. Use before, not prior to. Use use, not utilize.
- No analogies. State the fact directly. An analogy forces the reader to map two things instead of reading one.
- Avoid jargon and abstract metaphor nouns. Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. These read as technical but usually have a plainer concrete word. "Substrate" becomes "base". "Wedge in" becomes "add". "Vector" becomes "way" or "method". "Gold-plating" becomes "more than the job needs". "Ratchet" becomes the mechanism's real name or "a limit that only tightens". "Evacuate" becomes "move out". "Endgame" becomes "the last phase". Pick the concrete word.
- Prefer short, direct sentences over long compound ones. Split a sentence that carries two separate facts.
- Prefer the plain form of a word over the abstract one when both mean the same thing.
- Use active voice by default: "the parser reads the file", not "the file is read by the parser".
- Fragments and dropped grammar are fine only in true labels (list items, changelog lines, state names) where a full sentence would add nothing. Any explanation, reasoning, or step with a condition gets full sentences.
- Avoid em dashes mid sentences. They don't read human.

## Word-cutting rule

Cut a word only if removing it does not lower readability. Keep a word if cutting it would force the reader to guess, re-read, or fill in a gap.

Generally safe to cut:
- Filler: just, really, basically, actually, essentially, simply. "In order to" becomes "To". "Due to the fact that" becomes "Because".
- Excessive hedging. "could potentially possibly be argued that it might" becomes "may"
- Pleasantries: sure, certainly, happy to, of course.
- Throat-clearing: "it is worth noting that", "I want to point out that".
- Redundant qualifiers: "completely finished" becomes "finished".
- Fancy ways to say "is". "serves as", "stands as", "boasts", "features". Just say "is" or "has".

## Check before sending

- Does every word add to the reader's understanding, or just to sentence length?
- Did the same idea get a different word somewhere else in this text? If so, pick one and make it consistent.
- Would a shorter, more common word say the same thing?
- Can the reader get the point on one read, with no backtracking?

## Reasoning is not visible to the reader

Internal reasoning (a model's chain-of-thought, an intermediate scratchpad) is not shown to the reader. Do not assume a term, shorthand, or conclusion from that reasoning is already known. Restate or define, in the final text, anything the reader needs to follow it.

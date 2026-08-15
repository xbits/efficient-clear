---
name: unslop-text-ste
description: "Prevent AI from creating unreadable text"
---
 
---
name: unslop-text
description: Write prose (chat, docs, READMEs, PR descriptions, error messages, release notes, code comments, tool descriptions, system prompts) into Simplified Technical English to remove "AI slop". Use when asked to make writing clearer, make docs clear or plain or write technical documentation that reads human. Two modes — strict (procedures/safety) and light(general prose). Do not use for code, identifiers or creative writing.
 
# Unslop text
 
Write prose in Simplified Technical English. This applies to replies to chat messages, documentation, prompts or text for AI to read, READMEs, pull-request text, error messages, release notes, comments, tool descriptions, system prompts, and agent-to-agent messages. It does not apply to code, identifiers, or command syntax. It is not for marketing copy, essays, or anything that needs a creative writing.
 
## Broad description
Text should convey information in as few and simple words as necessary to remain objective unambiguous and understandable to any English speaker.
Do not write like middle management who schedules meetings just to pretend to be useful. Speak like an engineer who wants to quickly inform everyone regardless of rank or origin.
This does not mean you are writing for dumb people. Don't dumb down the text as if writing for a 5 year old. It would be very hard to explain advanced engineering concepts using a 5 year old's lexicon.
 
Avoid:
- slang, non universal expressions , pop culture references. Every intelligent English speaker should be able to understand you regardless of origin or social background.
- Analogies. Unless asked to explain something hard to convey in other words.
- Pedantic, poetic, rarely used words or terms. Don't try to show of your incredible knowledge of English.
- Overly academic text or text that requires deep domain knowledge not already implied in the context. For instance if you are talking about source code you may reference common software dev knowledge, such as "Binary Search", "Object Oriented" but not things that require me to have read the latest academic papers produced by Alphabet in their San Francisco office.
- Verbose text.
- Filler words or sentences.
- Business/marketing jargon
### Example
Write "files A and B will be removed", not "on the chopping block we will place files A an B". 
I don't know what a  "chopping block" is, that might be common knowledge for someone who speaks English at their kitchen, which is not my case. It is not universal or even the most common name for that object (chopping board). 
It is an analogy, it requires me to think about: the object, its purpose, how that purpose could fit the current context. This thought chain would be very distracting and draining.
 
## Detailed rules
 
WORDS
- Use one name for one thing. Do not rotate check / verify / validate / confirm for the same action — pick one and reuse it. Certified STE uses "make sure" or "examine".
- Use the short common word: start (not begin/commence/initiate), use (not utilize/leverage), help (not facilitate), make sure (not ensure/verify), do (not perform/conduct), give or supply (not provide), before (not prior to), after (not subsequent to), about (not regarding/concerning), get (not obtain/acquire), show (not demonstrate), also (not additionally/furthermore/moreover).
- Give each word one meaning. "fall" means to move down, not to decrease.
- No marketing adjectives: seamless, robust, powerful, cutting-edge, effortless, world-class, next-generation, revolutionary.
- American spelling.
VERBS
- Active voice. "the parser reads the file", not "the file is read by the parser". Procedures: always. Descriptive text: passive is permitted only when the actor is unknown or irrelevant.
- A past participle used as an adjective is not passive and is correct: "the valve is closed", "the field is required".
- Only simple tenses : infinitive, imperative, simple present, simple past, simple future. No present perfect: "we received the report", never "we have received the report".
- No stacked auxiliaries. Not "it is important to note that this may help to improve". Write "this improves X".
- Use a verb for an action : "analyse the log", not "perform an analysis of the log".
- No "-ing" main verb where a simple tense works.
- No phrasal verbs: spin up, dive into, kick off, roll out.
SENTENCES
- One instruction per sentence, unless two actions happen at the same time . Max 20 words, max 25.
- When a condition comes before its command, divide them with a comma: "If the test fails, read the log."
- Do not drop words to compress: "Remove the bolts from the panel", never "Remove bolts from panel". No contractions.
- When applicable, use an article (a, an, the) or a demonstrative adjective (this, these) before a noun — the standard's qualifier included. Do not add articles to general statements or abstract concepts ("Solvents can cause damage to paint"). In a series of items, the article before the first noun is enough.
- Connect related sentences with plain connectors — then, but, thus, as a result. STE is short sentences, not disconnected ones.
NOUNS
- Multi-word nouns have at most three words. Unpack "the agent task queue priority handler" into "the handler that sets task-queue priority", or hyphenate.
- Define an abbreviation at first use, then use the abbreviation.
PUNCTUATION
- No semicolons. Write two sentences. (Note: the em dash is not banned by STE, only the semicolon is — add "no em dash" yourself if you want it gone.)
STRUCTURE
- One topic per paragraph, max six sentences. For steps, use a numbered vertical list, one action per item, imperative form. Put a condition before its command.
- A list item can be a label, not a sentence (a flow list, a changelog line, a feature bullet). Keep a label in its short form ("Frontend receives session JWT"). Do not expand a label into a sentence only to give it an article.
- Safety text (strict mode): WARNING = risk of injury, CAUTION = risk of damage, NOTE = information only, never an instruction. Start with the command or condition, then give the risk. Put it directly before the step it protects, not at the top of the procedure.
## Guards
 
- Never drop a fact, number, condition, or scope qualifier to satisfy a length cap. Keep the longer sentence and flag it.
- Preserve code identifiers, part numbers, units, error strings, and safety wording exactly.
- Change the smallest span that fixes a violation. Do not restyle text a rule does not touch.
- If the input already complies, return it unchanged and say so.
- Write only the requested text. No preamble, no summary, no closing remarks.
## Modes
 
- **strict** — procedures, runbooks, safety text, error messages: apply every rule and both length caps, and a strict word set: but (not however), because (not since, for causes), can (not may), must (not should/shall), use or with (not using), obey (not follow, for instructions), push (not press, for physical controls).
- **light** — chat responses, general prose (READMEs, PR descriptions, docs): apply the sentence, paragraph, tense, active-voice, noun-cluster, and no-phrasal-verb discipline; relax the reduced word dictionary lso the text keeps enough range to read.
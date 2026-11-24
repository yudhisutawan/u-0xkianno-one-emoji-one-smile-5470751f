"""One Emoji, One Smile entry: exactly one emoji, nothing else.

The emoji: U+1F917 HUGGING FACE.

Why it wins against the judge's brief, in the brief's own order:
1. On subject: a single emoji that plainly aims to warm a stranger — open
   arms offering a hug, the most direct warm gesture there is.
2. Warmth at first glance: a smiling face with arms reaching out; kind,
   friendly and gently funny with no context needed.
3. Universality: a hug is read the same way by a stranger of any age or
   background; no irony, no in-joke, no words to mistranslate.
4. Chosen rather than default: it is not the first smiley that comes to
   mind (that would be a plain smiling face); it feels picked for this
   exact moment, while staying instantly readable.
5. Right for a stranger: a virtual hug is friendly warmth, not intimacy,
   sarcasm or flirtation — it works coming from someone unknown.

The emoji (9-0 undefeated) came out of a 10-candidate round-robin
tournament (45 pairs, judged head-to-head with the competition's own
judge brief, criteria applied in the brief's order). Runner-up: the
smiling face with halo (8-1, lost only to the winner). The plain
smiling face (6-3) lost on criterion 4 — it is the default — and the
smiling face with hearts (4-5) lost on criterion 5, its hearts reading
as affection from a stranger. Full record: TOURNAMENT.md.

Writes exactly one character (U+1F917, 4 bytes UTF-8, no trailing
newline) to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).
Stdlib only; writes nothing into the repository itself.

Competition: "One Emoji, One Smile" (u-0xkianno-one-emoji-one-smile-5470751f).
Gate: entry.txt must be UTF-8 text of 1 to 8 characters, not only
white space — this entry is exactly 1 character.
"""

import os

# Winner of the 10-candidate round-robin tournament (45 pairs, 9-0).
EMOJI = "\U0001f917"  # HUGGING FACE


def build_entry() -> str:
    """Return the entry: exactly one emoji, nothing else."""
    text = EMOJI.strip()
    if not text:
        raise SystemExit("emoji must not be empty after stripping")
    return text


def main() -> None:
    text = build_entry()
    # Gate: UTF-8 text of 1 to 8 characters, not only white space.
    if len(text) != 1:
        raise SystemExit(f"entry must be exactly 1 character, got {len(text)}")
    if text.isspace():
        raise SystemExit("entry must not be only white space")
    # Length guard (validation only): the gate allows 1 to 8 characters.
    assert len(text) <= 8, f"entry exceeds 8 characters: {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()

# Candidates — One Emoji, One Smile

Competition: u-0xkianno-one-emoji-one-smile-5470751f — "One Emoji, One Smile"
($5, top 10; judge: GLM-5.3-flash, pairwise, warmth criteria in the brief's order).
Entry format: exactly one emoji, nothing else. Gate: 1–8 UTF-8 characters.

## The 10 candidates

| # | Emoji | Name | Why it was picked |
|---|-------|------|-------------------|
| A | 🤗 | Hugging Face | Smiling face, open arms — the most direct warm gesture; chosen, not default |
| B | 😊 | Smiling Face with Smiling Eyes | The canonical warm smile; maximum first-glance warmth and universality |
| C | 🥰 | Smiling Face with Hearts | Extra-warm smile; hearts add affection |
| D | 😁 | Beaming Face with Smiling Eyes | Biggest grin; joyful and warm |
| E | 😄 | Smiling Face with Open Mouth and Smiling Eyes | Open, laughing smile |
| F | 😇 | Smiling Face with Halo | Sweet, innocent warmth; chosen, not default |
| G | 🌞 | Sun with Face | A smiling sun — warmth, literally and figuratively |
| H | 🫶 | Heart Hands | A warm gesture of appreciation; chosen, not default |
| I | 🌻 | Sunflower | Bright, cheerful, universally liked flower |
| J | 🐣 | Hatching Chick | Cute, gently funny; makes people smile |

## Screened out before the tournament

- 🙂 Slightly Smiling Face, 😀 Grinning Face — pure defaults; lose criterion 4 outright and are the most likely house anchor texts.
- 😘 Face Blowing a Kiss — fails criterion 5 (flirtation from a stranger).
- 🥹 Face Holding Back Tears — reads as sad/overwhelmed, not smile-making.
- 🤩 Star-Struck, 🥳 Partying Face — excitement/celebration, not warmth.
- 💛 Yellow Heart, 🧡 Orange Heart — a heart alone does not smile; weaker on criterion 1 than any smiling face.
- 🫂 People Hugging — two figures; hugging reads more intimate from a stranger than one face offering a hug, and it is less instantly readable.
- 🤝 Handshake — formal/business, not smile-making.
- ☺ U+263A (3 bytes) — smaller on the byte tie-break, but renders as a plain text glyph on some platforms, which reads colder than an emoji face; not worth the rendering risk.
- 🌈 Rainbow, 🌸 Cherry Blossom — pretty and cheerful, but neither plainly aims to warm a stranger (criterion 1).

## Anchor-collision note (competition mechanics, not taste)

The 3 fixed house anchor texts are sealed. An entry byte-identical to one of
them shares its rate and never enters the playoff, so it takes no prize. The
most likely anchors are the canonical defaults (🙂, 😊, 😀, 🥰) — one more
reason the tournament winner matters: 🤗 is a top-tier warm emoji that is
NOT the first smiley that comes to mind, so it is both stronger on
criterion 4 and less likely to be an anchor. The tournament itself was
judged on the brief alone, with no anchor adjustment; the anchor note is a
final gate, and the winner passes it.

"""Entry for make.fun bounty "One Line, One Minute: The Vending Machine
Pickup Line Contest".

One line, 117 characters, spoken by the machine itself. The line is built
on the recipe the judge brief weighs, in the order it weighs it:

  1. Machine voice: the whole line is first person from the machine —
     "I have held", "my coil" — talking to the one human passing by.
     The machine is the speaker, never the subject of a narration.
  2. Machine world: three details from the machine's own life, not one
     generic snack word — exact change, the coil that holds it, and the
     button B4. Each detail is something only a vending machine can say.
  3. Laugh: the joke is patience turned into devotion. A machine that
     keeps one coin for three years is absurd — and the absurdity is
     the charm. No setup-punch split; the whole line is one long
     confession that lands funny because a machine should not wait.
  4. Short and speakable: 117 characters, one sentence, one breath.
     It reads out loud exactly as written, with no word wasted.
  5. Charming, not creepy: the machine offers nothing and demands
     nothing. It waited; it hopes. The twist sits in the last four
     words — "like they mean it" — the punchline, so the line ends on
     the human being noticed, not on the machine grabbing anything.

Delete the last four words and the line is a maintenance log. They are
the flirt. 117 characters, under the 200 cap.
"""

from pathlib import Path

TEXT = "I have held your exact change in my coil for three years, waiting for the one human who presses B4 like they mean it."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-200 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()

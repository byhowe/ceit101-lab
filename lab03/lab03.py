# Pig latin translator

import sys

VOWELS = "aeiou"


def pig_latin(word: str) -> str:
    if word[0] in VOWELS:
        # vowel
        return word + "way"
    else:
        # consonant
        i = next(i for i, c in enumerate(word) if c in VOWELS)
        return word[i:] + word[:i] + "ay"


while True:
    word = input("Enter a word ('quit' to quit): ").strip().lower()
    match word:
        case "quit":
            break
        case "":
            print("Can't convert empty string.  Try again.", file=sys.stderr)
        case _:
            word = pig_latin(word)
            print(word)

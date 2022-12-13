from collections import Counter
from collections.abc import Iterable
from operator import itemgetter
import itertools
import os.path
import string
import sys


def get_file() -> str:
    while True:
        f = input("File to read -> ")
        if not f or not os.path.isfile(f):
            print(f"Failed to read {f}! Please try again.", file=sys.stderr)
            continue
        return f


def display_counts(counts: Iterable[tuple[str, int]]):
    print("{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in counts:
        print("{:15s}{:>5d}".format(item[0], item[1]))


doc = get_file()
with open(doc, "rt") as f:
    words = itertools.chain.from_iterable(line.split() for line in f)
    words = (word.strip(string.punctuation).lower() for word in words)
    words = (word for word in words if word)
    counts = Counter(words).items()
    counts = sorted(counts, key=itemgetter(0))
    counts = sorted(counts, key=itemgetter(1), reverse=True)

display_counts(counts)

from collections import Counter
from collections.abc import Iterable
from typing import Generator
import os.path
import sys

BENFORD = [
    None,  # First digit cannot be 0
    30.1,  # 1
    17.6,  # 2
    12.5,  # 3
    9.7,  # 4
    7.9,  # 5
    6.7,  # 6
    5.8,  # 7
    5.1,  # 8
    4.6,  # 9
]

# (digit, percentage, benford_percentage)
Count = tuple[int, float, float]


def first_digit(a: str) -> int:
    num = (int(x) for x in a if x.isdigit() and x != "0")
    return next(num)


def read_digits(path: str) -> Generator[int, None, None]:
    with open(path, "rt") as f:
        lines = (l.strip() for l in f)
        lines = (first_digit(l) for l in lines if l and l != "0")
        yield from lines


def count(digits: Iterable[int]) -> list[Count]:
    counts = Counter(digits)
    size = sum(counts.values())
    return [
        (i, round((counts[i] / size) * 100, ndigits=1), BENFORD[i])
        for i in range(1, 10)
    ]


def display(counts: list[Count]):
    print("{:>5s} {:>7s} {:>6s}".format("Digit", "Percent", "Benford"))
    for c in counts:
        print("{:>4d}: {:>6.1f}% ({:>4.1f}%)".format(*c))


while True:
    path = input("Path to the data set boss -> ")
    if os.path.isfile(path):
        break
    print(f"Failed to detect a file named {path} boss!", file=sys.stderr)

digits = read_digits(path)
counts = count(digits)
display(counts)

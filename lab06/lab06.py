# Exam grades

from typing import Callable, Generator
from collections.abc import Iterable

StudentInfo = tuple[str, int, int, int, int, float]


def mean(seq: Iterable[StudentInfo], key: Callable[[StudentInfo], int]) -> float:
    vals = list(key(e) for e in seq)
    return sum(vals) / len(vals)


def load(filepath: str) -> Generator[StudentInfo, None, None]:
    with open(filepath, "rt") as f:
        splitlines = (l.split() for l in f)
        for e in splitlines:
            name = e[0] + ' ' + e[1]
            scores = list(map(int, e[2:]))
            mean = sum(scores) / len(scores)
            yield (name, *scores, mean)


scores = list(load("scores.txt"))
scores.sort(key=lambda e: e[0])

e1mean = mean(scores, key=lambda e: e[1])
e2mean = mean(scores, key=lambda e: e[2])
e3mean = mean(scores, key=lambda e: e[3])
e4mean = mean(scores, key=lambda e: e[4])

o = "{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}"
print(o.format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
o = "{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}"
for e in scores:
    print(o.format(e[0], e[1], e[2], e[3], e[4], e[5]))
o = "{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}"
print(o.format("Exam Mean", e1mean, e2mean, e3mean, e4mean))

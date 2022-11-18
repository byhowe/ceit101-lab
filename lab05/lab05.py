# file parser

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Generator
import functools
import sys


@dataclass
class person:
    name: str
    height: float
    weight: float

    @property
    def bmi(self):
        return self.weight / self.height**2


def openlines(filepath: str) -> Generator[str, None, None]:
    with open(filepath, "r") as f:
        next(f)
        yield from f


def load(filepath: str) -> Generator[person, None, None]:
    return (
        person(l[0:12].strip(), float(l[12:24]), float(l[24:36]))
        for l in openlines(filepath)
    )


def save(
    persons: Iterable[person],
    avg_height: float,
    avg_weight: float,
    avg_bmi: float,
    max_height: float,
    max_weight: float,
    max_bmi: float,
    min_height: float,
    min_weight: float,
    min_bmi: float,
    file=sys.stdout,
):
    print("{:12s}{:12s}{:12s}{:12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"), file=file)
    for p in persons:
        print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(p.name, p.height, p.weight, p.bmi), file=file)
    print(file=file)
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", avg_height, avg_weight, avg_bmi), file=file)
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", max_height, max_weight, max_bmi), file=file)
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min_height, min_weight, min_bmi), file=file)

persons = list(load("data.txt"))

max_height = max(p.height for p in persons)
min_height = min(p.height for p in persons)
sum_height = sum(p.height for p in persons)
avg_height = sum_height / len(persons)

max_weight = max(p.weight for p in persons)
min_weight = min(p.weight for p in persons)
sum_weight = sum(p.weight for p in persons)
avg_weight = sum_weight / len(persons)

max_bmi = max(p.bmi for p in persons if p.bmi is not None)
min_bmi = min(p.bmi for p in persons if p.bmi is not None)
sum_bmi = sum(p.bmi for p in persons if p.bmi is not None)
avg_bmi = sum_bmi / len(persons)

output = functools.partial(
    save,
    persons,
    avg_height,
    avg_weight,
    avg_bmi,
    max_height,
    max_weight,
    max_bmi,
    min_height,
    min_weight,
    min_bmi,
)

# output to sys.stdout
output(file=sys.stdout)

# # write to a file
with open("output.txt", "w") as f:
    output(file=f)

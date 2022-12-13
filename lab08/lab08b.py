import itertools

Scores = dict[str, int]


def read_scores(path: str) -> Scores:
    with open(path, "rt") as f:
        return {
            s[0]: int(s[1]) for s in (l.split() for l in itertools.islice(f, 1, None))
        }


def sum_scores(a: Scores, b: Scores):
    for k, v in b.items():
        if k not in a:
            a[k] = 0
        a[k] += v


def display_scores(a: Scores):
    print("{:10s} {:10s}".format("Name", "Total"))
    for k, v in a.items():
        print("{:10s} {:<10d}".format(k, v))


a = read_scores("data1.txt")
b = read_scores("data2.txt")
sum_scores(a, b)
display_scores(a)

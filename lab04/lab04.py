# Leap year, rotate, digit count, float check


def leap_year(year: str) -> bool:
    n = int(year)
    return n % 400 == 0 or n % 4 == 0 and not n % 100 == 0


def rotate(s: str, n: int) -> str:
    return s[-n:] + s[:-n] if n < len(s) else s


def digit_count(n: int | float) -> tuple[int, int, int]:
    count_even: int = 0
    count_odd: int = 0
    count_zero: int = 0
    if int(n) == 0:
        return (0, 0, 0)
    for c in str(int(n)).split(".")[0]:
        match c:
            case "2" | "4" | "6" | "8":
                count_even += 1
            case "1" | "3" | "5" | "7" | "9":
                count_odd += 1
            case "0":
                count_zero += 1
    return (count_even, count_odd, count_zero)


def float_check(s: str) -> bool:
    a = s.split(".")
    if len(a) > 2:
        return False
    for digits in a:
        if digits == "":
            continue
        if not digits.isdigit():
            return False
    return True


expected_leap_year = {
    "1896": True,
    "1904": True,
    "2000": True,
    "1900": False,
}

expected_rotate = {
    ("abcdefgh", 3): "fghabcde",
}

expected_digit_count = {
    1234567890123: (5, 7, 1),
    123400.345: (2, 2, 2),
    123.0: (1, 2, 0),
    0.123: (0, 0, 0),
}

expected_float_check = {
    "1234": True,
    "123.45": True,
    "123.45.67": False,
    "34e46": False,
    ".45": True,
    "45.": True,
    "45..": False,
}


def tests():
    results_leap_year = (leap_year(k) == v for k, v in expected_leap_year.items())
    results_rotate = (rotate(*k) == v for k, v in expected_rotate.items())
    results_digit_count = (digit_count(k) == v for k, v in expected_digit_count.items())
    results_float_check = (float_check(k) == v for k, v in expected_float_check.items())

    print(f"{list(results_leap_year)=}")
    print(f"{list(results_rotate)=}")
    print(f"{list(results_digit_count)=}")
    print(f"{list(results_float_check)=}")


# tests()

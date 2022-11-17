# Compute the roots of a quadratic equation.

import math

print("ax^2 + bx + c")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(f"({a})x^2 + ({b})x + {c}")

delta = b**2 - 4 * a * c

if delta >= 0:
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
else:
    print("roots are imaginary")

# Count even and odd numbers enetered on the terminal.

import sys

even_sum: int = 0
even_count: int = 0

odd_sum: int = 0
odd_count: int = 0

while True:
    # get an input from the user
    n = int(input("Input an integer (0 terminates): "))
    if n < 0:
        print("Negative values are not accepted!", file=sys.stderr)
        continue
    elif n == 0:
        break

    # count the number
    match n % 2:
        case 0:
            even_sum += n
            even_count += 1
        case 1:
            odd_sum += n
            odd_count += 1

# output the results
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", even_count + odd_count)

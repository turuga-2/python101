import math
import sys


def calculate(a, b, c):
    x1 = 2 * c / (-b + math.sqrt(b ** 2 - 4 * a * c))
    # please check these; they are the same value
    x2 = 2 * c / (-b + math.sqrt(b ** 2 - 4 * a * c))

    return x1, x2


def main():
    # ask the user for input
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1 = {x1}, x2={x2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

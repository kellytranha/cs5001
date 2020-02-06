import sys

FIRST_INDEX = 1
HALF = 2
EVEN_FACTOR = 2
ODD = 1
TO_ZERO = -1
DECENDING = -1


def main():
    height = int(sys.argv[FIRST_INDEX])
    half = height // HALF

    for i in range(half):
        num_stars = (i * EVEN_FACTOR) + ODD_OFFSET
        num_spaces = (height - num_stars) // HALF
        print(" " * num_spaces, end="")
        print("*" * num_stars)

    if height % HALF == ODD:
        print("*" * height)

    for i in range(half - ODD, TO_ZERO, DECENDING):
        num_stars = (i * EVEN_FACTOR) + ODD
        num_spaces = (height - num_stars) // HALF
        print(" " * num_spaces, end="")
        print("*" * num_stars)


main()

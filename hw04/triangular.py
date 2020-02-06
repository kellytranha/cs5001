import sys

SECOND_INDEX = 1
ZERO = 0
NEXT_INDEX = 1


def main():

    total = ZERO
    entry = int(sys.argv[SECOND_INDEX])

    for i in range(SECOND_INDEX, entry + NEXT_INDEX):
        total += i

    print("The triangular number is", total)


main()

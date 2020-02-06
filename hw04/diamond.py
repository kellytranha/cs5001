import sys


def main():
    height = int(sys.argv[1])
    half = height // 2

    for i in range(half):
        num_stars = (i * 2) + 1
        num_spaces = (height - num_stars) // 2
        print(" " * num_spaces, end="")
        print("*" * num_stars)

    if height % 2 == 1:
        print("*" * height)

    for i in range(half - 1, -1, -1):
        num_stars = (i * 2) + 1
        num_spaces = (height - num_stars) // 2
        print(" " * num_spaces, end="")
        print("*" * num_stars)


main()

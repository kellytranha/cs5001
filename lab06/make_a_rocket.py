import sys

EVEN_FACTOR = 2
ODD_FACTOR = 1
ONE = 1  # draw 1 star
TWO = 2  # draw 2 stars


def nose_cone(width):
    if width % EVEN_FACTOR == ODD_FACTOR:
        star = ONE
    else:
        star = TWO

    space = (width - ODD_FACTOR) // EVEN_FACTOR
    for _ in range(space):
        print(" " * space, end="")
        print("*" * star, end="")
        print(" " * space)
        space -= ODD_FACTOR
        star += EVEN_FACTOR


def fuselage(width, length, striped=False):
    chr_to_draw = "_" if striped else "X"
    for _ in range(int(length)):
        for _ in range(width // EVEN_FACTOR):
            print(chr_to_draw * width)
        for _ in range(width - width // EVEN_FACTOR):
            print("X" * width)


def tail(width):
    space = (width - ODD_FACTOR) // (ODD_FACTOR + EVEN_FACTOR)
    star = width - EVEN_FACTOR * space
    for _ in range(space):
        print(" " * space, end="")
        print("*" * star, end="")
        print(" " * space)
        space -= ODD_FACTOR
        star += EVEN_FACTOR
    print("*" * width)
    print("*" * width)


def main(width, length, striped=False):
    nose_cone(width)
    fuselage(width, length, striped)
    tail(width)


if len(sys.argv) == 3:
    main(int(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 4 and sys.argv[3] == "striped":
    main(int(sys.argv[1]), int(sys.argv[2]), striped=True)
ODD_FACTOR = 1
EVEN_FACTOR = 2
INITIAL_SPACE = 0


def print_space(space):
    print(" " * space, end="")


def horizon(n, ending):
    print("+", end="")
    print("-" * EVEN_FACTOR * n, end="")
    print("+", end=ending)


def surface(n, space2, last, symbol):
    print(symbol, end="")
    print(" " * EVEN_FACTOR * n, end="")
    print(symbol, end="")
    print(" " * space2, end="")
    print(last)


def main():
    n = int(input("Input cube size (multiple of 2):"))
    space = int(n / EVEN_FACTOR) + ODD_FACTOR
    print_space(space)
    horizon(n, "\n")

    space -= ODD_FACTOR
    space2 = INITIAL_SPACE
    for i in range(int(n / EVEN_FACTOR)):
        print_space(space)
        surface(n, space2, "|", "/")
        space -= ODD_FACTOR
        space2 += ODD_FACTOR

    horizon(n, "")
    print_space(space2)
    print("|")

    for i in range(int(n / EVEN_FACTOR) - ODD_FACTOR):
        surface(n, space2, "|", "|")
    surface(n, space2, "+", "|")

    for i in range(int(n / EVEN_FACTOR)):
        space2 -= ODD_FACTOR
        surface(n, space2, "/", "|")

    horizon(n, "\n")


main()

import math

PYTHAGOREAN_CONST = 2
DOUBLE = 2


def draw_circle(x, y, r):
    if math.sqrt((x-r)**PYTHAGOREAN_CONST + (y-r)**PYTHAGOREAN_CONST) < r:
        print("o", end="")
    else:
        print(" ", end="")


def main():

    radius = int(input())

    for y in range(DOUBLE*radius):
        for x in range(DOUBLE*radius):
            draw_circle(x, y, radius)
        print()


main()

import sys

SECOND_INDEX = 1
THIRD = 2


def fibonacci(n):
    first = 0
    second = 1
    if n <= first:
        print(first)
    elif n == second:
        print(second)
    else:
        print(first)
        print(second)
        for i in range(THIRD, n):
            temp = first + second
            first = second
            second = temp
            print(temp)


def main():

    entry = int(sys.argv[SECOND_INDEX])
    fibonacci(entry)


main()

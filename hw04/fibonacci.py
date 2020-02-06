import sys


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def main():

    entry = int(sys.argv[1])
    for i in range(0, entry):
        x = fibonacci(i)
        print(x)


main()

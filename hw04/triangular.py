import sys


def main():

    total = 0
    entry = int(sys.argv[1])

    for i in range(1, entry+1):
        total += i

    print("The triangular number is", total)


main()

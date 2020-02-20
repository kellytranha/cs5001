import sys

SECOND_INDEX = 1
ZERO = 0
NEXT_INDEX = 1


def triangular_number(entry):
    total = 0
    for i in range(SECOND_INDEX, int(entry) + NEXT_INDEX):
        total += i
    print("The triangular number for", entry, "is", total)
    return total


def main():

    final_list = []
    entry = input("Enter a number, or enter 'done':")

    while entry != "done":
        final_list.append(triangular_number(entry))
        entry = input("Enter a number, or enter 'done':")

    print(final_list)


main()

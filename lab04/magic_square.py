SUM = 15


def equal_total(num1, num2, num3, total):
    return int(num1) + int(num2) + int(num3) == total


def main():
    first = input("Enter a magic number: \n")
    second = input()
    third = input()

    if equal_total(first[0], first[1], first[2], SUM) and \
            equal_total(second[0], second[1], second[2], SUM) and \
            equal_total(third[0], third[1], third[2], SUM) and \
            equal_total(first[0], second[0], third[0], SUM) and \
            equal_total(first[1], second[1], third[1], SUM) and \
            equal_total(first[2], second[2], third[2], SUM) and \
            equal_total(first[0], second[1], third[2], SUM) and \
            equal_total(first[2], second[1], third[0], SUM):
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()

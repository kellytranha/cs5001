ZERO = 0
ONE = 1
NINE = 9
REVERSE = -1


def equal_len(list1, list2):
    while len(list1) < len(list2):
        list1.append("0")

    while len(list1) > len(list2):
        list2.append("0")


def carries_count(list1, list2):
    carries = ZERO
    carry = ZERO
    for i in range(len(list1)):
        if (int(list1[i]) + int(list2[i])) + carry > NINE:
            carry = ONE
            carries += ONE
        else:
            carry = ZERO
    return carries


def main():

    num1 = input("Enter the first number:")
    list1 = list(num1)[::REVERSE]
    num2 = input("Enter the second number:")
    list2 = list(num2)[::REVERSE]

    print(num1, "+", num2, "=", int(num1) + int(num2))
    equal_len(list1, list2)
    print("Number of carries", carries_count(list1, list2))


main()

import sys

TENTH = 10
REVERSE = -1
EVEN = 2
DIVISIBLE = 0
DOUBLE = 2
LARGEST_DIGIT = 9
STARTING_VALUE = 0
SECOND_INDEX = 1


def check_isdigit(string):
    # check if the input only contains digits
    for c in string:
        if not c.isdigit():
            return False
    return True


def two_digit(num):
    # add the first digit of that value to the second digit,
    # yielding a single digit number
    first = int(num // TENTH)
    second = int(num % TENTH)
    return first + second


def make_list(num):
    # create a list of digits and reverse order
    reverse_list = list(num)[::REVERSE]
    # convert to list of integers
    new_list = [int(_) for _ in reverse_list]
    return new_list


def validate(a_list):
    # Double every other digit from the second digit
    # If the resulting number is a two digit number,
    # add the first digit of that value to the second digit,
    # yielding a single digit number.
    sum_list = []
    for index, value in enumerate(a_list, start=SECOND_INDEX):
        if index % EVEN == DIVISIBLE:
            value *= DOUBLE
            if value > LARGEST_DIGIT:
                value = two_digit(value)
        sum_list.append(value)

    # Add the sum of the modified digits to the sum of the digits
    # from the original sequence which were skipped over in step 1.
    sum_of_num = STARTING_VALUE
    for i in sum_list:
        sum_of_num += i

    # If the resulting sum is evenly divisible by 10, the sequence is valid.
    # If the resulting sum is not divisible by 10, the sequence is not valid.
    if sum_of_num % TENTH == DIVISIBLE:
        print("The sequence is valid.")
    else:
        print("The sequence is not valid.")


def main(num):
    while not check_isdigit(num):
        print("Not a valid input\n")
        return
    validate(make_list(num))


main(sys.argv[SECOND_INDEX])

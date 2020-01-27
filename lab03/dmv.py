import random

DL_LENGTH = 7
SMALLEST_DIGIT = 0
BIGGEST_DIGIT = 9
EXP_YEAR = "21"


def main():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    fullname = input("Please enter your first, middle, and last name:\n")
    dob = input("Enter date of birth (MM/DD/YY):\n")

    dl = ""
    for _ in range(DL_LENGTH):
        y = str(random.randint(SMALLEST_DIGIT, BIGGEST_DIGIT))
        dl += y

    name_break = fullname.rfind(" ")
    last = fullname[name_break + 1:]
    first = fullname[:name_break]
    exp = dob[:6] + EXP_YEAR

    print("-------------------------------------")
    print("Washington Driver License")
    print("DL", dl)
    print("LN", last)
    print("FN", first)
    print("DOB", dob)
    print("EXP", exp)
    print("-------------------------------------")


main()

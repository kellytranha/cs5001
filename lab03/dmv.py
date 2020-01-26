import random
import string

def main():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    fullname = input("Please enter your first, middle, and last name:\n")
    dob = input("Enter date of birth (MM/DD/YY):\n")

    dl = "".join(random.choice('0123456789') for x in range(7))
    name_break = fullname.rfind(" ")
    last = fullname[name_break + 1:]
    first = fullname[:name_break]
    exp = dob[0:6]+"21"

    print("-------------------------------------")
    print("Washington Driver License")
    print("DL", dl)
    print("LN", last)
    print("FN", first)
    print("DOB", dob)
    print("EXP", exp)
    print("-------------------------------------")

main()
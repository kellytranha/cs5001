# Kelly Tran - Write code that uses input to read
# the user's first name, last name, and favorite word,
# prompting them each time so that they know what to enter.

import random

SMALLEST_DIGIT = 0
BIGGEST_DIGIT = 99


def main():
    print("Welcome to the username and password generator!")
    first = input("Please enter your first name: ")  # get First Name
    last = input("Please enter your last name: ")  # get Last Name
    last_long = last + "********"  # add *
    fav = input("Please enter your favorite word: ")  # get fav
    y = str(random.randint(SMALLEST_DIGIT, BIGGEST_DIGIT))  # get random number 0-99
    username = first[0] + last_long[:7] + y # generate username
    passwordx = (first + y + last).lower()
    password1 = passwordx.replace("a", "@").replace("o", "0").replace("l", "1").replace("s", "$") #get password1
    password2 = first[0].lower() + first[-1].upper() + last[0].lower() + last[-1].upper() + fav[0].lower() + fav[-1].upper()  # generate password2
    password3 = randint(SMALLEST_DIGIT, len(first))  # get password3

    print("Thanks", first, "your user name is", username.lower())

    print("Here are three suggested passwords for you to consider:")

    print("Password 1: ", password1)
    print("Password 2: ", password2)
    # print("Password 3: ", password3)


main()

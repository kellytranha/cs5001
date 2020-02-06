# Kelly Tran - Write code that uses input to read
# the user's first name, last name, and favorite word,
# prompting them each time so that they know what to enter.

from random import randint

SMALLEST_DIGIT = 0
BIGGEST_DIGIT = 99
FIRST_INDEX = 0
EIGHTH_INDEX = 7
LAST_INDEX = -1
SECOND_INDEX = 1


def main():
    print("Welcome to the username and password generator!")
    first = input("Please enter your first name: ")  # get First Name
    last = input("Please enter your last name: ")  # get Last Name
    last_long = last + "********"  # add *
    fav = input("Please enter your favorite word: ")  # get fav
    y = str(randint(SMALLEST_DIGIT, BIGGEST_DIGIT))  # get random number 0-99

    # generate username
    username = first[FIRST_INDEX] + last_long[:EIGHTH_INDEX] + y

    # generate password1: concatenation of the user's first and last names,
    # in lower case, with a random integer in the range 0 – 99 between them
    # All a characters should be replaced by @, o by 0, l by 1, and s by $
    passwordx = (first + y + last).lower()
    password1 = passwordx.replace("a", "@").replace("o", "0").\
        replace("l", "1").replace("s", "$")

    # generate password2: consisting of the first and last character from
    # the user's first name, the first and last character of their last name,
    # and the first and last letter of their favorite word. In each case,
    # the first letter of the pair should be lower case and the second should
    # be upper case.
    password2 = first[FIRST_INDEX].lower() + first[LAST_INDEX].upper() +\
        last[FIRST_INDEX].lower() + last[LAST_INDEX].upper() +\
        fav[FIRST_INDEX].lower() + fav[LAST_INDEX].upper()

    # generate password3: The third password takes a random-length portion
    # of the first name, combined with random-length portions of the favorite
    # word and last name. those random-length pieces should start at the
    # beginning of the string, and the code should be written such that it's
    # possible to get the entire string if the largest possible random number
    # is produced. At least one character from each part (first name, last
    # name, and favorite word) should appear in the password.
    password3 = first[:randint(SECOND_INDEX, len(first))] +\
        fav[:randint(SECOND_INDEX, len(fav))] +\
        last[:randint(SECOND_INDEX, len(last))]

    print("Thanks", first, "your user name is", username.lower())
    print("Here are three suggested passwords for you to consider:")
    print("Password 1: ", password1)
    print("Password 2: ", password2)
    print("Password 3: ", password3)


main()

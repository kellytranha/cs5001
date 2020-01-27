import random

MIN_DIGIT = 1
MAX_DIGIT = 50

FIRST_COUNT = 1

SCALDING_HOT = 1
EXTREMELY_WARM = 2
VERY_WARM = 3
WARM = 5
COLD = 8
VERY_COLD = 13
EXTREMELY_COLD = 20

LUCKY = 1
AMAZING_LOW = 2
AMAZING_HIGH = 4
OKAY_LOW = 5
OKAY_HIGH = 6
MEH = 7
NOT_GAME_LOW = 8
NOT_GAME_HIGH = 9


def main():
    print("Welcome to the Guessing Game!")
    print("I picked a number between 1 and 50. Try and guess!")

    secret = random.randint(MIN_DIGIT, MAX_DIGIT)
    guess = int(input(""))
    tries = FIRST_COUNT
    dif = abs(secret - guess)

    while (guess != secret):
        tries += 1
        if dif <= SCALDING_HOT:
            print("You guessed", guess)
            print("Your guess is scalding hot")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= EXTREMELY_WARM:
            print("You guessed", guess)
            print("Your guess is extremely warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= VERY_WARM:
            print("You guessed", guess)
            print("Your guess is very warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= WARM:
            print("You guessed", guess)
            print("Your guess is warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= COLD:
            print("You guessed", guess)
            print("Your guess is cold")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= VERY_COLD:
            print("You guessed", guess)
            print("Your guess is very cold")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= EXTREMELY_COLD:
            print("You guessed", guess)
            print("Your guess is extremely cold")
            guess = int(input(""))
            dif = abs(secret - guess)

        else:
            print("You guessed", guess)
            print("Your guess is icy freezing miserably cold")
            guess = int(input(""))
            dif = abs(secret - guess)

    print("Congratulations. You figured it out in", tries, "tries.")

    if tries == LUCKY:
        print("That was lucky!")

    elif AMAZING_LOW <= tries <= AMAZING_HIGH:
        print("That was amazing!")

    elif OKAY_LOW <= tries <= OKAY_HIGH:
        print("That was okay.")

    elif tries == MEH:
        print("Meh.")

    elif NOT_GAME_LOW <= tries <= NOT_GAME_HIGH:
        print("This is not your game.")

    else:
        print("You are the worst guesser I've ever seen.")


main()

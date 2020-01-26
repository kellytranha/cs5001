import random

def main():
    print("Welcome to the Guessing Game!")
    print("I picked a number between 1 and 50. Try and guess!")
    
    secret = random.randint(1, 50)
    print(secret)
    guess = int(input(""))
    tries = 1
    dif = abs(secret - guess)

    while (guess != secret):
        tries += 1
        if dif <= 1:
            print("You guessed", guess)
            print("Your guess is scalding hot")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 2:
            print("You guessed", guess)
            print("Your guess is extremely warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 3:
            print("You guessed", guess)
            print("Your guess is very warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 5:
            print("You guessed", guess)
            print("Your guess is warm")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 8:
            print("You guessed", guess)
            print("Your guess is cold")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 13:
            print("You guessed", guess)
            print("Your guess is very cold")
            guess = int(input(""))
            dif = abs(secret - guess)

        elif dif <= 20:
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

    if (guess == secret):
        if tries == 1:
            print("That was lucky!")
        
        elif 2<=tries<=4:
            print("That was amazing!")
        
        elif 5<=tries<=6:
            print("That was okay.")
        
        elif tries == 7:
            print("Meh.")
        
        elif 8<=tries<=9:
            print("This is not your game.")

        else:
            print("You are the worst guesser I've ever seen.")
            
main()

NUM_OF_STAR = 1
NUM_OF_SIDE = 2
NUM_OF_SPACE = 1


def is_valid(n):  # check if number is odd
    if n > 0 and (n % 2 != 0):
        return True
    return False


def main():
    base = int(input("Please enter an odd positive integer: "))

    while not is_valid(base):
        base = int(input("Not valid. Please enter an odd positive integer: "))

    height = int((base - NUM_OF_STAR)/NUM_OF_SIDE - NUM_OF_STAR)
    space = int((base - NUM_OF_STAR)/NUM_OF_SIDE)
    print(" "*space, end="")
    print("*")

    space -= NUM_OF_SPACE
    space_middle = NUM_OF_STAR

    for i in range(height):
        print(" "*space, end="")
        print("/", end="")
        print(" "*space_middle, end="")
        print("\\", end="\n")
        space -= NUM_OF_SPACE
        space_middle += NUM_OF_SIDE

    print("/", end="")
    print("_"*(base - NUM_OF_SIDE), end="")
    print("\\", end="\n")


main()

def is_valid(n):  # check if number is odd
    if n > 0 and (n % 2 != 0):
        return True
    return False


def main():
    base = int(input("Please enter an odd positive integer: "))

    while not is_valid(base):
        base = int(input("Not valid. Please enter an odd positive integer: "))

    height = int((base - 3)/2)
    space = int((base - 1)/2)
    print(" "*space, end="")
    print("*", end="\n")

    space -= 1
    space_middle = 1

    for i in range(height):
        print(" "*space, end="")
        print("/", end="")
        print(" "*space_middle, end="")
        print("\\", end="\n")
        space -= 1
        space_middle += 2

    print("/", end="")
    print("_"*(base-2), end="")
    print("\\", end="\n")


main()

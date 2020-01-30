MIN_DIGIT = 2
LINES_FULL_SYMBOLS = 2


def main():
    symbol = input("Enter symbol you would like to use: ")
    width = int(input("Enter the width: "))

    while width < MIN_DIGIT:
        width = int(input("Please enter the width not lower than 2: "))

    height = int(input("Enter the height: "))

    while height < MIN_DIGIT:
        height = int(input("Please enter the width not lower than 2: "))

    for _ in range(width):
        print(symbol, end="")
    print()

    for _ in range(height-LINES_FULL_SYMBOLS):
        print(symbol, end="")
        print(" "*(width-LINES_FULL_SYMBOLS), end="")
        print(symbol, end="\n")

    for _ in range(width):
        print(symbol, end="")
    print()


main()

def main():
    string = input("Give a string with any capitalization: ").lower()
    to_be_replaced = "aeiou"

    for character in to_be_replaced:
        string = string.replace(character, character.upper())

    print(string)


main()

def main():
    string = input("Give a string with any capitalization: ").lower()

    for x in string:
        if x == 'A' or x == 'a' or x == 'E' or x == 'e' \
        or x == 'I' or x == 'i' or x == 'O' or x == 'o' \
        or x == 'U' or x == 'u':
            string = string.replace(x, x.upper())

    print(string)

main()
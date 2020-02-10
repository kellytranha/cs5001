def main():

    name = input("Enter the file name: ")  
    try:
        out = open(name, "r")
    except Exception:
        print("Can't open ", name)
        return

    content = out.read()

    word_count = len(content.split())

    content_no_space = content.replace(" ", "").replace("\n", "")

    content_alphanumeric = 0
    for ch in content:
        if ch.isalnum():
            content_alphanumeric += 1

    print("Words: ", word_count)
    print("Characters: ", len(content_no_space))
    print("Letters & numbers: ", content_alphanumeric)


main()

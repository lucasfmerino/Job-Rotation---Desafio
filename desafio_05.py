def reverse (text):
    reverse_text = text[::-1]
    print(reverse_text)
    return reverse_text


if __name__ == "__main__":

    text = input("Write something to reverse: ")

    reverse(text)


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = text.replace(",", " ")
    text = text.replace("...", " ")
    text = text.lstrip(" ")

    if " " in text:
        text = text.split(" ")
    else:
        text = text.split(".")

    print(text)
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")

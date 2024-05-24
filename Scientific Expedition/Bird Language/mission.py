VOWELS = "aeiouy"


def translation(phrase):
    result = ''
    while True:
        try:
            letter = next(iter(phrase))
        except StopIteration:
            return result
        if letter == ' ':
            phrase = phrase[1:]
        elif letter not in VOWELS:
            phrase = phrase[2:]
        else:
            phrase = phrase[3:]
        result += letter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translation("hieeelalaooo") == "hello", "Hi!"
    assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translation("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translation("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

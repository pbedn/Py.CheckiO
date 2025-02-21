from string import punctuation

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    for p in punctuation:
        text = text.replace(p, ' ')
    striped = text.upper().split()
    for word in striped:
        if len(word) == 1:
            continue
        ok = True
        for i in range(len(word) - 1):
            if (not (word[i] in CONSONANTS and word[i + 1] in VOWELS or
                     word[i + 1] in CONSONANTS and word[i] in VOWELS)):
                ok = False
        if ok:
            count += 1
    return count


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

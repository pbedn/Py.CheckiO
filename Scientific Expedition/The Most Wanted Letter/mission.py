import string
from operator import itemgetter

A = string.ascii_lowercase


def checkio(text):
    if len(text) == 1:
        return text.lower()
    counter = {}
    single = True
    for l in text.lower():
        if l in A:
            try:
                counter[l] += 1
                single = False
            except KeyError:
                counter[l] = 1
    res = sorted(counter.items(), key=itemgetter(1), reverse=True)
    if single:
        x = sorted(res, key=lambda x: ord(x[0]))[0][0]
        return x[0][0].lower()
    rr = res[0]
    tmp = []
    for r in res:
        if r[1] == rr[1]:
            tmp.append(r)
    if len(tmp) > 1:
        x = sorted(tmp, key=lambda x: ord(x[0]))[0][0]
        return x[0][0].lower()
    return res[0][0].lower()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

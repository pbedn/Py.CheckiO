def checkio(number):
    res = 1
    for x in str(number):
        if x == "0":
            continue
        res *= int(x)
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

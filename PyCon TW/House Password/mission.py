from string import ascii_lowercase


def checkio(data):
    res, res2, res3 = False, False, False
    for d in data:
        if d in ascii_lowercase:
            res = True
        if d in ascii_lowercase.upper():
            res2 = True
        if d in '0123456789':
            res3 = True

    return len(data) >= 10 and res and res2 and res3


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

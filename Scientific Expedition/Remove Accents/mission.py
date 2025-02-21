import unicodedata


def checkio(in_string):
    """remove accents"""
    normal = unicodedata.normalize('NFKD', in_string).encode('ASCII', 'ignore')
    if not normal:
        return in_string
    return normal.decode('utf-8')

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')

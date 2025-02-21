VALUES = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}


def worth_of_words(words):
    best_word = ''
    best_sum = 0
    for w in words:
        sum = 0
        for l in w:
            sum += VALUES[l]
        if sum > best_sum:
            best_word = w
            best_sum = sum
    return best_word


if __name__ == '__main__':
    print("Example:")
    print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")

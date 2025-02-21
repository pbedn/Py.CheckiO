from collections import Counter
from itertools import chain


def frequency_sort(items):
    """
    Counter.most_common([n])
        Return a list of the n most common elements
        and their counts from the most common to the least
    chain.from_iterable(iterable)
        Gets chained inputs from a single iterable argument that is evaluated lazily
    """
    return chain.from_iterable([v[0]] * v[1] for v in Counter(items).most_common())


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

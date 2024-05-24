def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    data = sorted(data)
    list_of_intervals, interval = [], []
    for i in range(len(data)):
        try:
            if data[i] + 1 == data[i + 1]:
                interval.append(data[i])
                continue
        except IndexError:
            pass
        interval.append(data[i])
        list_of_intervals.append((min(interval), max(interval)))
        interval = []
    return list_of_intervals


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')

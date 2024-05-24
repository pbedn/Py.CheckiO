def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if not line: return 0
    last = line[0]
    s = []
    ss = ''
    for l in line:
        if l != last:
            s.append([ss])
            ss = ''
            last = l
        ss += l
    # print(max([len(w[0]) for w in s]))
    if not s:
        return len(line)
    return max([len(w[0]) for w in s])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

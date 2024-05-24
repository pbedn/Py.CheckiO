def find_subs(line):
    subs = ''
    for letter in line:
        if letter not in subs:
            subs += letter
            continue
        else:
            break
    return subs


def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if set(line) == line:
        return line
    longest = ''
    for i in range(len(line)):
        subs = find_subs(line[i:])
        if len(subs) > len(longest):
            longest = subs
    return longest


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')

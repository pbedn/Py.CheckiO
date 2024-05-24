def second_index(text: str, symbol: str):
    seen = []
    for i, t in enumerate(text):
        if t in seen and t == symbol:
            return i
        seen.append(t)
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    assert second_index("hi", "i") == None
    print('You are awesome! All tests are done! Go Check it!')

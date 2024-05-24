def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    pos_end = text.find(end) if text.find(end) >= 0 else len(text)
    pos_begin = text.find(begin) + len(begin) if text.find(begin) >= 0 else 0
    return text[pos_begin:pos_end]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')

LETTERS = 'abcdefgh'


def check_left_bottom_pawn(p, pawns):
    letter_loc = LETTERS.index(p[0])
    new_letter = LETTERS[letter_loc - 1] if letter_loc > 0 else False
    new_index = str(int(p[1]) - 1) if int(p[1]) > 1 else False
    if new_letter and new_index:
        new_pawn = "{}{}".format(new_letter, new_index)
        return new_pawn in pawns
    return False


def check_right_bottom_pawn(p, pawns):
    letter_loc = LETTERS.index(p[0])
    new_letter = LETTERS[letter_loc + 1] if letter_loc < 7 else False
    new_index = str(int(p[1]) - 1) if int(p[1]) > 1 else False
    if new_letter and new_index:
        new_pawn = "{}{}".format(new_letter, new_index)
        return new_pawn in pawns
    return False


def safe_pawns(pawns):
    count = 0
    for p in pawns:
        safe1 = check_left_bottom_pawn(p, pawns)
        safe2 = check_right_bottom_pawn(p, pawns)
        if safe1 or safe2:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

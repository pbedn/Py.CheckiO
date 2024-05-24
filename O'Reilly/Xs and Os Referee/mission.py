def check_result(pattern, game_result):
    winners = ['X', 'O']
    for i, j, k in pattern:
        w = game_result[i]
        if game_result[j] == w and game_result[k] == w and w in winners:
            return w
    return False


def checkio(game_result):
    game_result = [y for x in game_result for y in x]
    horizontal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    vertical = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
    diagonal = ((0, 4, 8), (2, 4, 6))

    for pattern in (horizontal, vertical, diagonal):
        res = check_result(pattern, game_result)
        if res:
            return res
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

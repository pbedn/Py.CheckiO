from typing import List


def checkio(land_map: List[List[int]]) -> int:
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 1, 1, 1, 0, 1, 1],
                   [1, 1, 1, 1, 0, 0, 1],
                   [1, 1, 1, 1, 1, 0, 1],
                   [1, 1, 0, 1, 1, 0, 1],
                   [1, 1, 0, 1, 1, 1, 1],
                   [1, 0, 0, 1, 1, 1, 1],
                   [1, 0, 1, 1, 1, 1, 1]]))

    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")

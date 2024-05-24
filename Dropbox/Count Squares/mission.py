def count_squares(points: list[tuple[int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(count_squares([(0, 0), (1, 0), (0, 1), (1, 1)]))

# These "asserts" are used for self-checking
assert count_squares([(0, 0), (1, 0), (0, 1), (1, 1)]) == 1
assert (
        count_squares(
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        )
        == 6
)
assert (
        count_squares(
            [
                (4, 3),
                (1, 1),
                (5, 3),
                (2, 3),
                (3, 2),
                (3, 1),
                (4, 2),
                (2, 1),
                (3, 3),
                (1, 2),
                (5, 2),
            ]
        )
        == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

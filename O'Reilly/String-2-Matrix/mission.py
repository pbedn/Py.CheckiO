Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]


def converter(text: str) -> Grid:
    # your code here
    return tuple()


print("Example:")
print(converter("sMcigkqow"))

# These "asserts" are used for self-checking
assert converter("sMcigkqow") == (
    (0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (1, 0, 2, 0, 1),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0),
)
assert converter("acSyIwoQkumGe") == (
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

def highest_building(buildings: list[list[int]]) -> list[int]:
    # your code here
    return []


print("Example:")
print(highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))

# These "asserts" are used for self-checking
assert highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
    3,
    4,
]
assert highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == [
    4,
    1,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")

from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

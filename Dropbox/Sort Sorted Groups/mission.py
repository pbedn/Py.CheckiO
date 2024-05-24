def sorted_groups(items: list[int]) -> list[int]:
    # your code here
    return []


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")

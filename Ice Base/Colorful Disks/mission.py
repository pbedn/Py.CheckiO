def count_discs(discs: tuple[int, ...]) -> int:
    # your code here
    return 0


print("Example:")
print(count_discs((3, 2)))

# These "asserts" are used for self-checking
assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
assert count_discs((6, 5, 4, 3, 2, 1)) == 6
assert count_discs((5,)) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

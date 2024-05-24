def safe_squares(n: int, bishops: tuple[int, int]) -> int:
    # your code here
    return 0


print("Example:")
print(safe_squares(10, []))

# These "asserts" are used for self-checking
assert safe_squares(10, []) == 100
assert safe_squares(4, [(2, 3), (0, 1)]) == 11
assert safe_squares(8, [(1, 1), (3, 5), (7, 0), (7, 6)]) == 29

print("The mission is done! Click 'Check Solution' to earn rewards!")

def reach_corner(x: int, y: int, m: int, n: int, aliens: list[tuple[int, int]]) -> bool:
    # your code here
    return False


print("Example:")
print(reach_corner(0, 2, 5, 5, []))

# These "asserts" are used for self-checking
assert reach_corner(0, 2, 5, 5, []) == False
assert reach_corner(4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)]) == False
assert reach_corner(1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

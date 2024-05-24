def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    # your code here
    return False


print("Example:")
print(squares_intersect((2, 2, 3), (5, 5, 2)))

# These "asserts" are used for self-checking
assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

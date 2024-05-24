def hourglass_flips(glasses: list[tuple[int, int]], t: int) -> int | None:
    # your code here
    return 0


print("Example:")
print(hourglass_flips([(1, 0), (2, 0)], 2))

# These "asserts" are used for self-checking
assert hourglass_flips([(1, 0), (2, 0)], 2) == 0
assert hourglass_flips([(7, 0), (11, 0)], 15) == 2
assert hourglass_flips([(4, 0), (6, 0)], 11) == None
assert hourglass_flips([(7, 1), (10, 4), (13, 1), (18, 4)], 28) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")

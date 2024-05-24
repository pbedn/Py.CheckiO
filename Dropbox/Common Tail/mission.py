def common_tail(a: list[int], b: list[int]) -> int | None:
    # your code here
    return 0


print("Example:")
print(common_tail([1, 2, 3, 4], [5, 6, 3, 4]))

# These "asserts" are used for self-checking
assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3
assert common_tail([1, 3, 4, 6], [2, 9, 4, 6]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

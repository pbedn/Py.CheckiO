def calkin_wilf(n: int) -> tuple[int, int]:
    # your code here
    return 1, 1


print("Example:")
print(calkin_wilf(2))

# These "asserts" are used for self-checking
assert calkin_wilf(1) == (1, 1)
assert calkin_wilf(2) == (1, 2)
assert calkin_wilf(3) == (2, 1)
assert calkin_wilf(10) == (3, 5)
assert calkin_wilf(100) == (7, 19)

print("The mission is done! Click 'Check Solution' to earn rewards!")

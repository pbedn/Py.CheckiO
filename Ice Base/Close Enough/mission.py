def hitting_powers(a: int, b: int, tol: int = 100) -> tuple[int, int] | list[int]:
    # your code here
    return ()


print("Example:")
print(hitting_powers(9, 10, 5))

# These "asserts" are used for self-checking
assert list(hitting_powers(9, 10, 5)) == [1, 1]
assert list(hitting_powers(2, 4, 100)) == [2, 1]
assert list(hitting_powers(2, 7, 100)) == [73, 26]
assert list(hitting_powers(3, 6, 100)) == [137, 84]

print("The mission is done! Click 'Check Solution' to earn rewards!")

def cleaning_robot(cap: int, start: str, bat: str, junk: str) -> float:
    # your code here
    return 0


print("Example:")
print(cleaning_robot(1, "E", "A", "C"))

# These "asserts" are used for self-checking
assert cleaning_robot(1, "E", "A", "C") == 0.0
assert cleaning_robot(1, "E", "B", "C") == 0.25
assert cleaning_robot(2, "E", "A", "B") == 0.0625

print("The mission is done! Click 'Check Solution' to earn rewards!")

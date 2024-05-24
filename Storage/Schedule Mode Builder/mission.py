def schedule(tasks: list[str], mode: int) -> list[str]:
    # your code here
    return []


print("Example:")
print(
    schedule(
        ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 1
    )
)

# These "asserts" are used for self-checking
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 1
) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 2
) == ["09:00-10:00", "10:00-11:00"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 3
) == ["09:00-10:00", "10:00-11:00"]
assert schedule(
    ["09:00-10:00", "09:50-10:10", "10:00-11:00", "09:00-09:20", "10:50-11:10"], 4
) == ["09:00-09:20", "09:50-10:10", "10:50-11:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 1
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 2
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 3
) == ["09:00-10:00", "10:00-10:10"]
assert schedule(
    ["09:00-10:00", "10:00-10:10", "09:10-09:20", "09:30-09:40", "09:50-10:00"], 4
) == ["09:10-09:20", "09:30-09:40", "09:50-10:00", "10:00-10:10"]

print("The mission is done! Click 'Check Solution' to earn rewards!")

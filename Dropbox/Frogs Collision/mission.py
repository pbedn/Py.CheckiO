Frog = tuple[int, int, int, int]


def frogs_collision(frog1: Frog, frog2: Frog) -> int | None:
    # your code here
    return 0


print("Example:")
print(frogs_collision((0, 0, 0, 2), (0, 10, 0, 1)))

# These "asserts" are used for self-checking
assert frogs_collision((0, 0, 0, 2), (0, 10, 0, 1)) == 10
assert frogs_collision((10, 10, -1, 0), (0, 1, 0, 1)) == None
assert (
        frogs_collision(
            (620775675217287, -1862327025651882, -3, 9),
            (413850450144856, 2069252250724307, -2, -10),
        )
        == 206925225072431
)
assert frogs_collision((0, 0, 0, 0), (1, 1, 3, 3)) == None

print("The mission is done! Click 'Check Solution' to earn rewards!")

from collections.abc import Iterable


def flood_area(diagram: str) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(flood_area(r"\\//")))

# These "asserts" are used for self-checking
assert list(flood_area("\\\\//")) == [4]
assert list(flood_area("_/\\//")) == [1]
assert list(flood_area("\\\\/_")) == [1]
assert list(flood_area("\\\\_\\\\_/_/\\//_")) == [18]
assert list(flood_area("////\\\\_\\///__\\")) == [11]
assert list(flood_area("/\\\\\\\\_\\\\\\/\\\\_/\\\\\\_\\/\\/\\//_/\\/_///\\/////")) == [
    220
]
assert list(flood_area("\\____\\____\\/\\/\\\\____/_\\/_____/_/___/\\_")) == [84]

print("The mission is done! Click 'Check Solution' to earn rewards!")

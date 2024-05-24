def sort_digit_count(items: list[int]) -> list[int]:
    # your code here
    return []


print("Example:")
print(sort_digit_count([99, 123456789, 10 ** 10]))

# These "asserts" are used for self-checking
assert sort_digit_count([99, 123456789, 10000000000]) == [10000000000, 123456789, 99]
assert sort_digit_count([9876, 19, 4321, 99, 73, 241, 111111, 563, 33]) == [
    111111,
    33,
    241,
    4321,
    563,
    73,
    19,
    9876,
    99,
]
assert sort_digit_count([111, 19, 919, 1199, 911, 999]) == [
    111,
    19,
    911,
    919,
    1199,
    999,
]
assert sort_digit_count([1234, 4321, 3214, 2413]) == [1234, 2413, 3214, 4321]

print("The mission is done! Click 'Check Solution' to earn rewards!")

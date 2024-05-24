def changing_direction(elements: list[int]) -> int:
    change = 0
    direction = None
    first = elements[0]
    for i, second in enumerate(elements[1:]):
        if first == second:
            continue
        elif first < second:
            if direction == 1:
                change += 1
            direction = 0
        else:
            if direction == 0:
                change += 1
            direction = 1
        first = second
    return change


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

from math import e, pi


def checkio(n: float) -> str:
    # your code here
    return ""


print("Example:")
print(checkio(5.85987448205))

# These "asserts" are used for self-checking
assert checkio(5.85987448205) == "e+pi"
assert checkio(18.2958548951) == "e**e+pi"
assert checkio(47.6085189284) == "e**e*pi"
assert checkio(-0.42331082513) == "e-pi"
assert checkio(7.38905609893) == "e*e"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def repeat_inside(line: str) -> str:
    # your code here
    return ""


print("Example:")
print(repeat_inside("aaaaa"))

# These "asserts" are used for self-checking
assert repeat_inside("aaaaa") == "aaaaa"
assert repeat_inside("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""
assert repeat_inside("abcabcabab") == "abcabc"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def remove_brackets(line: str) -> str:
    # your code here
    return ""


print("Example:")
print(remove_brackets("(()()"))

# These "asserts" are used for self-checking
assert remove_brackets("(()()") == "()()"
assert remove_brackets("[][[[") == "[]"
assert remove_brackets("[[(}]]") == "[[]]"
assert remove_brackets("[[{}()]]") == "[[{}()]]"
assert remove_brackets("[[[[[[") == ""
assert remove_brackets("[[[[}") == ""
assert remove_brackets("") == ""
assert remove_brackets("[(])") == "()"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def switch_strings(line: str, result: str) -> bool:
    # your code here
    return False


print("Example:")
print(switch_strings("btry", "byrt"))

# These "asserts" are used for self-checking
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

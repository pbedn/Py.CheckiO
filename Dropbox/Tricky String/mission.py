def tricky_string(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(tricky_string("Checkio"))

# These "asserts" are used for self-checking
assert tricky_string("checkIO") == "CheckIO"
assert tricky_string("zcheckzz") == "zCheckIO"
assert tricky_string("SoManyChoicesHere") == "SoManyCheckIOHere"

print("The mission is done! Click 'Check Solution' to earn rewards!")

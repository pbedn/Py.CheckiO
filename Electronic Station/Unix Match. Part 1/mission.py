def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    return True


print("Example:")
print(unix_match("somefile.txt", "*"))

# These "asserts" are used for self-checking
assert unix_match("somefile.txt", "*") == True
assert unix_match("other.exe", "*") == True
assert unix_match("my.exe", "*.txt") == False
assert unix_match("log1.txt", "log?.txt") == True
assert unix_match("log12.txt", "log?.txt") == False
assert unix_match("log12.txt", "log??.txt") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

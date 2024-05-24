from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(scytale_decipher("aaaatctwtkdn", "dawn"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (
            scytale_decipher("totetshpmeecisendysescwticsriasraytlaegphet", "sicret")
            == None
    ), "Crib is not in plaintext"
    assert (
            scytale_decipher("aaaatctwtkdn", "at") == None
    ), "More than one possible decryptions"

    print("Coding complete? Click 'Check' to earn cool rewards!")

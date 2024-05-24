from typing import List, Optional


def grille_encrypt(plaintext: str, grille: List[str]) -> Optional[str]:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
            grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."])
            == "actilangeslrdret"
    )
    assert (
            grille_encrypt(
                "quickbrownfoxjumpsoverthelazydog", ["X...", "...X", "..X.", ".X.."]
            )
            == "qxwkbnjufriumcoopyeerldsatoogvhz"
    )
    assert (
            grille_encrypt(
                "quickbrownfoxjumpsoverthelazydog", [".XX.", ".XX.", "..X.", "X..."]
            )
            == None
    )
    assert grille_encrypt("cardangrilletest", ["...X", "....", "....", "...."]) == None

    print("Coding complete? Click 'Check' to earn cool rewards!")

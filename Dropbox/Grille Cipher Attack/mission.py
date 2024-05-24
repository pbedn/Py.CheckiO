from typing import List


def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    # your code here
    return []


if __name__ == "__main__":
    print("Example:")
    print(
        find_grille(
            "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
            "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_grille(
        "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
        "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
    ) == [
               "XXXX....",
               "XXXX....",
               "XXXX....",
               "XXXX....",
               "........",
               "........",
               "........",
               "........",
           ]

    assert find_grille(
        "weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong",
        "wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz",
    ) == [
               "X...X...",
               ".X.....X",
               "..X...X.",
               "...X.X..",
               "X.....X.",
               "...X...X",
               "..X.X...",
               ".X...X..",
           ]

    assert find_grille(
        "theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv",
        "tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo",
    ) == [
               "X.......",
               ".X.....X",
               "X.....XX",
               ".X..X...",
               "XX......",
               "..XXX...",
               "..X....X",
               "...X....",
           ]

    print("Coding complete? Click 'Check' to earn cool rewards!")

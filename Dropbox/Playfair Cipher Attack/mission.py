def playfair_attack(plaintext: str, cryptogram: str) -> str:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
            playfair_attack(
                "sixcrazykingsvowedtoabolishmyquitepitifulioust",
                "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
            )
            == "vklprhcrixbpzebc"
    )

    assert (
            playfair_attack(
                "pythonsxstandardlibraryisveryextensiveofferingawiderangeofstuffx",
                "aiwblarskwphydowzehmhoieksxlixgwvufxlvzqvizxbehdycxlphyxzqkwcvsi",
            )
            == "dmhfiulxgbxvqhyx"
    )

    assert (
            playfair_attack(
                "zombiesquicklyatetwelveofmyneighboursx",
                "uzuywyksmzdcvhfgtnftonbnkfevywlgxzmxzd",
            )
            == "xnzpchtyrfcwpkth"
    )

    print("Coding complete? Click 'Check' to earn cool rewards!")

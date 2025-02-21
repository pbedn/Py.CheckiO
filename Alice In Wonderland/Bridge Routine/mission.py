def bridge_routine(
        hand: list[tuple[str, str]], trump="notrump"
) -> tuple[int, str] | list[int, str]:
    # your code here
    return []


print("Example:")
print(
    list(
        bridge_routine(
            [
                ("four", "spades"),
                ("five", "spades"),
                ("ten", "hearts"),
                ("six", "hearts"),
                ("queen", "hearts"),
                ("jack", "hearts"),
                ("four", "hearts"),
                ("two", "hearts"),
                ("three", "diamonds"),
                ("seven", "diamonds"),
                ("four", "diamonds"),
                ("two", "diamonds"),
                ("four", "clubs"),
            ],
            "diamonds",
        )
    )
)

# These "asserts" are used for self-checking
assert list(
    bridge_routine(
        [
            ("four", "spades"),
            ("five", "spades"),
            ("ten", "hearts"),
            ("six", "hearts"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("four", "hearts"),
            ("two", "hearts"),
            ("three", "diamonds"),
            ("seven", "diamonds"),
            ("four", "diamonds"),
            ("two", "diamonds"),
            ("four", "clubs"),
        ],
        "diamonds",
    )
) == [8, "xx QJxxxx xxxx x"]
assert list(
    bridge_routine(
        [
            ("three", "spades"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("eight", "hearts"),
            ("six", "diamonds"),
            ("nine", "diamonds"),
            ("jack", "diamonds"),
            ("ace", "diamonds"),
            ("nine", "clubs"),
            ("king", "clubs"),
            ("jack", "clubs"),
            ("five", "clubs"),
            ("ace", "clubs"),
        ],
        "clubs",
    )
) == [20, "x QJx AJxx AKJxx"]
assert list(
    bridge_routine(
        [
            ("three", "spades"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("eight", "hearts"),
            ("six", "diamonds"),
            ("nine", "diamonds"),
            ("jack", "diamonds"),
            ("ace", "diamonds"),
            ("nine", "clubs"),
            ("king", "clubs"),
            ("jack", "clubs"),
            ("five", "clubs"),
            ("ace", "clubs"),
        ],
        "spades",
    )
) == [17, "x QJx AJxx AKJxx"]

print("The mission is done! Click 'Check Solution' to earn rewards!")

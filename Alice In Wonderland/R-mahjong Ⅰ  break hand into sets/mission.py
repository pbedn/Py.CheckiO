def riichi_mahjong_sets(hand: list) -> list:
    # your code here
    return sorted([])  # you must sort resulting list before returning


print("Example:")
print(
    riichi_mahjong_sets(
        [
            "m2",
            "s9",
            "p9",
            "dg",
            "s3",
            "s2",
            "m1",
            "s8",
            "dg",
            "p9",
            "dg",
            "s7",
            "s1",
            "m3",
        ]
    )
)

# These "asserts" are used for self-checking
assert riichi_mahjong_sets(
    ["m7", "s6", "p2", "m9", "s5", "wn", "s3", "p4", "s4", "p3", "s5", "m8", "s7", "wn"]
) == ["m789", "p234", "s345", "s567", "wnn"]
assert riichi_mahjong_sets(
    ["s7", "p4", "s6", "m8", "m4", "m3", "m8", "m8", "m2", "p6", "m4", "s5", "p5", "m4"]
) == ["m234", "m44", "m888", "p456", "s567"]
assert riichi_mahjong_sets(
    ["s8", "s7", "p2", "s4", "s9", "s3", "s5", "s1", "s6", "m5", "s2", "p2", "m3", "m4"]
) == ["m345", "p22", "s123", "s456", "s789"]
assert riichi_mahjong_sets(
    ["s8", "s9", "m1", "ws", "dr", "s7", "dr", "m9", "ws", "m9", "m2", "dr", "m3", "ws"]
) == ["drrr", "m123", "m99", "s789", "wsss"]

print("Now, what about 'Check solution'?")

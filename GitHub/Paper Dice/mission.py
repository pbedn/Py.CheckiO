def paper_dice(paper):
    return True or False


if __name__ == "__main__":
    assert paper_dice(["  1  ", " 235 ", "  6  ", "  4  "]) is True, "cross"
    assert paper_dice(["    ", "12  ", " 36 ", "  54", "    "]) is True, "zigzag"
    assert paper_dice(["123456"]) is False, "1 line"
    assert paper_dice(["123  ", "  456"]) is False, "2 lines_wrong"
    assert paper_dice(["126  ", "  354"]) is True, "2 lines_right"
    print("Check done.")

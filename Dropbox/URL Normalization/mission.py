def checkio(url):
    return url


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("Http://Www.Checkio.org") == "http://www.checkio.org", "1st rule"
    assert (
            checkio("http://www.checkio.org/%cc%b1bac")
            == "http://www.checkio.org/%CC%B1bac"
    ), "2nd rule"
    assert (
            checkio("http://www.checkio.org/task%5F%31") == "http://www.checkio.org/task_1"
    ), "3rd rule"
    assert (
            checkio("http://www.checkio.org:80/home/") == "http://www.checkio.org/home/"
    ), "4th rule"
    assert (
            checkio("http://www.checkio.org:8080/home/")
            == "http://www.checkio.org:8080/home/"
    ), "4th rule again"
    assert (
            checkio("http://www.checkio.org/task/./1/../2/././name")
            == "http://www.checkio.org/task/2/name"
    ), "5th rule"
    print("First set of tests done")

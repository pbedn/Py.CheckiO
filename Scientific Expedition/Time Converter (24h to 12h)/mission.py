def time_converter(time):
    if time == '24:00':
        time = '00:00'
    hour, minute = time.split(":")
    if hour[0] == '0':
        hour = hour[1:]
    text = 'p' if int(hour) >= 12 else 'a'
    hour = hour if 0 < int(hour) <= 12 else str(abs(int(hour) - 12))
    return "{}:{} {}.m.".format(hour, minute, text)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

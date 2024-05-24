import calendar


def date_time(time: str) -> str:
    date, time = time.split(" ")
    day, month, year = date.split(".")
    hours, minutes = time.split(":")
    m = "s" if int(minutes) != 1 else ""
    h = "s" if int(hours) != 1 else ""
    return f"{int(day)} {calendar.month_name[int(month)]} {year} year {int(hours)} hour{h} {int(minutes)} minute{m}"


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"

print("The mission is done! Click 'Check Solution' to earn rewards!")

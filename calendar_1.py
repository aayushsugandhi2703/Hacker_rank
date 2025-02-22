import calendar

month, day, year = map(int, input().split())

day_index = calendar.weekday(year, month, day)

day_name = calendar.day_name[day_index].upper()

print(day_name)

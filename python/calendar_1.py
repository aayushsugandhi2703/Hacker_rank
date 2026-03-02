# this helps in finding out the day of the week for a given date
import calendar

month, day, year = map(int, input().split())

day_index = calendar.weekday(year, month, day)

day_name = calendar.day_name[day_index].upper()

print(day_name)

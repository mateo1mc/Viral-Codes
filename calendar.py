import calendar

def print_calendar_year(year):
    cal = calendar.TextCalendar().formatyear(year)
    print(cal)

year = 2024

print_calendar_year(year)


from enum import Enum

class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(repr(WeekDay.MONDAY))
print(repr(WeekDay(2)))
print(repr(WeekDay["WEDNESDAY"]))

print(WeekDay.THURSDAY.name)
print(WeekDay.THURSDAY.value)

for day in WeekDay:
    print(day.name, "->", day.value)
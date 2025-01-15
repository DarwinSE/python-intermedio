# Ejercicios con Fechas

from datetime import datetime

now  = datetime.now()

# timestamp = now.timestamp()
# print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2026 = datetime(2026, 1, 1)
print_date(year_2026)

print('///////////////////////')

from datetime import time

current_time = time(13, 15, 55)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print('///////////////////////')

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(2026, 1, 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(current_date.year + 7, current_date.month, current_date.day)
print(current_date.year)

print(year_2026 - now)
print(year_2026.date() - current_date)

print('///////////////////////')

from datetime import timedelta

start_timedelta = timedelta(216, 23, 56, weeks= 7)
end_timedelta = timedelta(216, 23, 56, weeks= 24)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
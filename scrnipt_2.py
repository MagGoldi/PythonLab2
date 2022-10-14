import datetime


today = str(datetime.date.today())
print(today)
yesterday = datetime.date(2022, 10, 13)
print(yesterday)
year, mounth, day = 2022, 10, 14
print(datetime.toordinal())

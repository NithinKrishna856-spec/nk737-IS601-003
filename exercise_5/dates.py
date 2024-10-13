from datetime import datetime, date, timedelta

#formatting datetime object into a string 
def my_datetime(dt: datetime) -> str:
    return dt.strftime("%Y %m %d %H %M %S")

#list all saturdays from today to till next year
def saturdays() -> list:
    today = date.today()
    #to find the next saturday
    next_saturday = today + timedelta(days=(5 - today.weekday()) % 7) #5 is saturday
    next_year = date(today.year + 1, 1, 1)
    saturdays_list = []
    while next_saturday < next_year:
        saturdays_list.append(next_saturday)
        next_saturday += timedelta(weeks=1)
    return saturdays_list

#to check if the saturday is 1st or 15th and not on a weekend
def first_or_fifteenth(dt: date) -> bool:
    return dt.day in [1, 15] and dt.weekday() < 5 

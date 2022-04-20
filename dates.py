import datetime
x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# create date time objects
import datetime
x = datetime.datetime(2022, 4, 20) # The datetime() class requires three parameters to create a date: year, month, day.
print(x)


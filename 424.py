import calendar
weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
user_input = input("Insert the Date (dd/mm/yyy): ")
day = user_input[0:2]
month = user_input[3:5]
year = user_input[-4:]
week_day = calendar.weekday(int(year), int(month), int(day) + 1)
print(weekdays[week_day])
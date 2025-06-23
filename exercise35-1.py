from datetime import datetime, date

# Today's date
today = date.today()
print("Today's Date:", today)

# Day of the week
print("Day of the Week:", today.strftime("%A"))

# Days until New Year
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print("Days until New Year:", days_left)


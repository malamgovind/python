from datetime import date, timedelta

today = date.today()

future = today + timedelta(days=30)

print(future)
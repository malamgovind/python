from datetime import date

today = date.today()

new_year = date(
    today.year + 1,
    1,
    1
)

days_left = new_year - today

print(days_left.days)
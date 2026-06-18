from datetime import datetime

date = datetime.strptime(
    "18-06-2026",
    "%d-%m-%Y"
)

print(date)

# "18-06-2026"
# ↓
# strptime()
# ↓
# datetime object   
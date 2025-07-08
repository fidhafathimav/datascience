from datetime import datetime, timedelta

date = datetime.today()
count = 0

while count < 5:
    date -= timedelta(days=1)
    if date.weekday() < 5:  # Mon-Fri are 0-4
        count += 1

print("Date 5 business days ago:", date.date())

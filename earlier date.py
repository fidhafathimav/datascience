from datetime import datetime

def earlier_date(date1_str, date2_str, date_format="%Y-%m-%d"):
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    if date1 < date2:
        return f"{date1_str} is earlier"
    elif date1 > date2:
        return f"{date2_str} is earlier"
    else:
        return "Both dates are the same"

d1 = "2025-07-08"
d2 = "2023-01-15"

print(earlier_date(d1, d2))
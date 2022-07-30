def is_leap(year):  # checkif leap
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1  # is leap
            else:
                return 0  # not leap
        else:
            return 1
    else:
        return 0


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days[1] += is_leap(year)
    return month_days[month - 1]


year = int(input("Enter a year:"))
month = int(input("Enter a month:"))
if month>1 and month<12:
    days = days_in_month(year, month)
    print(days)
else: print("invalid month!!")

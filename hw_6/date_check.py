"""This module checks the date to see if it can exist, and also checks the year for leap year.
"""


def check_date_exists(date_text):
    try:
        day, month, year = map(int, date_text.split('.'))
        if is_leap_year(year):
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return 1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]
    except ValueError:
        return False

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    date = input("Enter a date (in the format 'DD.MM.YYYY'): ")
    if check_date_exists(date):
        print("Date exists.")
    else:
        print("Date does not exist.")

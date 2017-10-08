"""
    Author: Xavier
    Date: 2017/10/8
    Function: Judge which day in a year
    Version: 4.0 use dict to replace tuple
"""
from datetime import datetime


def is_leap_year(year):
    """
        judge if the year is leap year
        yes, return True
        no, return False
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def main():
    """
        main function
    """
    input_date_str = input('input the date(yyyy/mm/dd):')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    month_days_dict = {1: 31,
                       2: 28,
                       3: 31,
                       4: 30,
                       5: 31,
                       6: 30,
                       7: 31,
                       8: 31,
                       9: 30,
                       10: 31,
                       11: 30,
                       12: 31}

    days = day

    for i in range(1, month):
        days += month_days_dict[i]

    if is_leap_year(year) and (month > 2):
        days += 1

    print("it's the {}rd day in {}".format(days, year))


if __name__ == '__main__':
    main()

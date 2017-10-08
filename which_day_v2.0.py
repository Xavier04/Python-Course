"""
    Author: Xavier
    Date: 2017/10/8
    Function: Judge which day in a year
    Version: 2.0 use list to replace tuple
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

    days_in_month_tup = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month_tup[1] = 29

    days = sum(days_in_month_tup[:month - 1]) + day

    print("it's the {}rd day in {}".format(days, year))


if __name__ == '__main__':
    main()

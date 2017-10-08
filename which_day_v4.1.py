"""
    Author: Xavier
    Date: 2017/10/8
    Function: Judge which day in a year
    Version: 4.1 use dict to replace tuple
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

    days_month_dict = {30: {4, 6, 9, 11},
                       31: {1, 3, 5, 7, 8, 10, 12}}

    days = day

    for i in range(1, month):
        if i in days_month_dict[30]:
            days += 30
        elif i in days_month_dict[31]:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and (month > 2):
        days += 1

    print("it's the {}rd day in {}".format(days, year))


if __name__ == '__main__':
    main()

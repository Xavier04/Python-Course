"""
    Author: Xavier
    Date: 2017/10/8
    Function: Judge which day in a year
    Version: 1.0
"""
from datetime import datetime


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

    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[:month - 1]) + day

    # judge the leap year
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days += 1

    print("it's the {}rd day in {}".format(days, year))


if __name__ == '__main__':
    main()

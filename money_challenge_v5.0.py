"""
    Date: 2017/9/28
    Author: Xavier
    Function: 52 weeks money challenge
    Version: 5.0
"""
import math
import datetime


def save_money_in_n_weeks(money_per_week, total_week, increase_money):

    money_list = []  # record
    save_money_list = []

    for i in list(range(total_week)):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        save_money_list.append(saving)

        # output
        # print('{} week save {} yuan, account {} yuan'.format(i + 1, money_per_week, saving))

        money_per_week += increase_money
    return save_money_list


def main():
    """
        main function
    """
    money_per_week = float(input('money_per_week:'))                 # money
    increase_money = float(input('increase_money:'))                 # increase money
    total_week = int(input('total_week:'))
    save_money_list = save_money_in_n_weeks(money_per_week, total_week, increase_money)

    # input the date to consult
    input_date_str = input('input date(yyyy/mm/dd):')
    # change date_str to datetime
    input_date = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    # get the week number
    week_num = input_date.isocalendar()[1]
    print('the {} week save {} yuan'.format(week_num, save_money_list[week_num - 1]))


if __name__ == '__main__':
    main()

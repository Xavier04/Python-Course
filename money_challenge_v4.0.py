"""
    Date: 2017/9/28
    Author: Xavier
    Function: 52 weeks money challenge
    Version: 4.0
"""
import math


def save_money_in_n_weeks(money_per_week, total_week, increase_money):

    money_list = []  # record

    for i in list(range(total_week)):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # output
        print('{} week save {} yuan, account {} yuan'.format(i + 1, money_per_week, saving))

        money_per_week += increase_money
    return saving


def main():
    """
        main function
    """
    money_per_week = float(input('money_per_week:'))                 # money
    increase_money = float(input('increase_money:'))                 # increase money
    total_week = int(input('total_week:'))

    saving = save_money_in_n_weeks(money_per_week, total_week, increase_money)
    print('out:', saving)


if __name__ == '__main__':
    main()

"""
    Date: 2017/9/28
    Author: Xavier
    Function: 52 weeks money challenge
    Version: 2.0
"""
import math


def main():
    """
        main function
    """
    money_per_week = 10                 # money
    i = 1                               # week
    increase_money = 10                 # increase money
    total_week = 52                     # total weeks
    # saving = 0                          # accumulate
    money_list = []                     # record

    while i <= total_week:
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # output
        print('{} week save {} yuan, account {} yuan'.format(i, money_per_week, saving))

        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()

"""
    Date: 2017/9/28
    Author: Xavier
    Function: 52 weeks money challenge
    Version: 3.0
"""
import math


def main():
    """
        main function
    """
    money_per_week = 10                 # money
    increase_money = 10                 # increase money
    money_list = []                     # record

    for i in list(range(52)):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # output
        print('{} week save {} yuan, account {} yuan'.format(i+1, money_per_week, saving))

        money_per_week += increase_money


if __name__ == '__main__':
    main()

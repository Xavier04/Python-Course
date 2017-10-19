"""
    Author: Xavier
    Date: 2017/10/15
    Function: simulate rolling two dices
    Version: 2.0
"""
import random


def main():
    """
        main function
    """
    total_times = 10000
    result_list = [0] * 11
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        # generate random int range 1~6
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        # count the number times
        roll_dict[roll1 + roll2] += 1

    for j, x in roll_dict.items():
        print('{} appears {} times, frequency {}'
              .format(j, x, x / total_times))


if __name__ == '__main__':
    main()

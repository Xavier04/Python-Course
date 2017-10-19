"""
    Author: Xavier
    Date: 2017/10/15
    Function: simulate rolling dice
    Version: 1.0
"""
import random


def main():
    """
        main function
    """
    total_times = 20
    result_list = [0]*6

    for i in range(total_times):
        # generate random int range 1~6
        roll = random.randint(1, 6)
        # count the number times
        result_list[roll - 1] += 1

    for j, x in enumerate(result_list):
        print('{} appears {} times, frequency {}'
              .format(j + 1, x, x / total_times))


if __name__ == '__main__':
    main()

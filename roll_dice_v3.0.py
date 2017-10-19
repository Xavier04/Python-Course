"""
    Author: Xavier
    Date: 2017/10/15
    Function: simulate rolling two dices
    Version: 3.0 plot the result
"""
import random
import matplotlib.pyplot as plt


def main():
    """
        main function
    """
    total_times = 100
    result_list = [0] * 11
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    # store the roll result
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        # generate random int range 1~6
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        # record the roll result
        roll1_list.append(roll1)
        roll2_list.append(roll2)

        # count the number times
        roll_dict[roll1 + roll2] += 1

    for j, x in roll_dict.items():
        print('{} appears {} times, frequency {}'
              .format(j, x, x / total_times))

    # show the dices result
    x = range(1, total_times+1)
    y1 = roll1_list
    y2 = roll2_list

    plt.scatter(x, y1, alpha=0.5)
    plt.scatter(x, y2, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()

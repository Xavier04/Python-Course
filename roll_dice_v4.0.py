"""
    Author: Xavier
    Date: 2017/10/15
    Function: simulate rolling two dices
    Version: 4.0 plot the result
"""
import random
import matplotlib.pyplot as plt

# if you want to show chinese in histogram
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        main function
    """
    total_times = 1000

    # initialize the result_list
    result_list = []

    for i in range(total_times):
        # generate random int range 1~6
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        result_list.append(roll1 + roll2)

    # plot the histogram
    plt.hist(result_list, bins=range(2, 14), edgecolor='black', linewidth=1, normed=1)
    # plt.title('dice result')
    # plt.xlabel('dice result')
    # plt.ylabel('frequency')
    plt.title('骰子统计')
    plt.xlabel('骰子点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()

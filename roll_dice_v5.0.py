"""
    Author: Xavier
    Date: 2017/10/15
    Function: simulate rolling two dices
    Version: 5.0 science calculate
"""
import matplotlib.pyplot as plt
import numpy as np

# if you want to show chinese in histogram
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        main function
    """
    total_times = 10000

    # initialize the result_list
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)

    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # plot the histogram
    plt.hist(result_arr, bins=range(2, 14), edgecolor='black', linewidth=1, normed=1, rwidth=0.8)

    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点'
                   ]
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.title('骰子统计')
    plt.xlabel('骰子点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()

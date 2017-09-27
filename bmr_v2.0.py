"""
    Date:2017/9/27
    Function:BMR Calculator
    Version:2.0
"""


def main():
    # y_or_n = input('exit(y/n):')
    # while y_or_n != 'y':
        gender = input('input gender(male/female):')

        weight = float(input('input weight(kg):'))

        height = float(input('input height(cm):'))

        age = float(input('input age:'))

        if gender == 'male':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'female':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('BMR:', bmr)
        else:
            print('not supported')

        print()
        y_or_n = input('exit(y/n):')
        while y_or_n != 'y':
            main()


if __name__ == '__main__':
    main()

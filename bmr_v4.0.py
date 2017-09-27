"""
    Date:2017/9/27
    Function:BMR Calculator
    Version:4.0 abnormal situation handle
"""


def bmr_cal(str_list):
    """
        function to calculate BMR
    """
    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == 'male':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'female':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('gender: {} weight: {}kg height: {}cm age: {}years'.format(gender, weight, height, age))
            print('BMR: {}ka'.format(bmr))
        else:
            print('not supported')

        print()

    except ValueError:
        print('input the correct message')
    except IndexError:
        print('input enough error')
    except:
        print('programme abnormal!')


def main():
    y_or_n = input('exit(y/n):')
    while y_or_n != 'y':
        print(' please input information, separate with space:')
        input_str = input('gender weight(kg) height(cm) age:')

        input_list = input_str.split(' ')
        # call bmr_cal function
        bmr_cal(input_list)

        y_or_n = input('exit(y/n):')


if __name__ == '__main__':
    main()

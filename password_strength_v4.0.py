"""
    Author: Xavier
    Date: 2017/10/10
    Function: check the password strength
    Version: 4.0 read the file
"""


# def check_number_exist(password):
#     """
#         check if the number exist in password
#     """
#     has_numeric = False
#     for c in password:
#         if c.isnumeric():
#             has_numeric = True
#             break
#     return has_numeric
#
#
# def check_letter_exist(password):
#     """
#         check if the letter exist in password
#     """
#     has_letter = False
#     for c in password:
#         if c.isalpha():
#             has_letter = True
#             break
#     return has_letter


def main():
    """
        main function
    """
    # try_times = 5
    #
    # while try_times > 0:
    #
    #     password_str = input('please input your password:')
    #
    #     strength_level = 0
    #
    #     # rule1: the password length no less than 8
    #     if len(password_str) >= 8:
    #         strength_level += 1
    #     else:
    #         print('the password length should be no less than 8')
    #
    #     # rule2: the password should include number
    #     if check_number_exist(password_str):
    #         strength_level += 1
    #     else:
    #         print('the password length should include number')
    #
    #     # rule3: the password should include letter
    #     if check_letter_exist(password_str):
    #         strength_level += 1
    #     else:
    #         print('the password length should include letter')
    #
    #     if strength_level == 0:
    #         strength_str = 'weak'
    #     elif strength_level == 1:
    #         strength_str = 'relatively weak'
    #     elif strength_level == 2:
    #         strength_str = 'relatively strong'
    #     else:
    #         strength_str = 'strong'
    #
    #     f = open('password.txt', 'a')
    #     f.write('password: {} strength: {}\n'.format(password_str, strength_str))
    #     f.close()
    #
    #     if strength_level == 3:
    #         print('the password is OK!')
    #         break
    #     else:
    #         print('the password is not OK!')
    #         try_times -= 1
    #
    #     print()
    #
    # if try_times <= 0:
    #     print('too many tries!!!')

    # 1. read()
    # f = open('password.txt', 'r')
    # content = f.read()
    # print(content)

    # 2. readline()
    # f = open('password.txt', 'r')
    # content = f.readline()
    # print(content)
    # content = f.readline()
    # print(content)

    # 3. readlines()
    # f = open('password.txt', 'r')
    # content = f.readlines()
    # print(content)

    # f = open('password.txt', 'r')
    # for i in f:
    #     print(i)

    # f = open('password.txt', 'r')
    # for i in f.read():
    #     print(i)

    # f = open('password.txt', 'r')
    # for i in f.readlines():
    #     print(i)

    f = open('password.txt', 'r')
    for i in f.readline():
        print(i)


if __name__ == '__main__':
    main()

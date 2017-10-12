"""
    Author: Xavier
    Date: 2017/10/09
    Function: check the password strength
    Version: 1.0
"""


def check_number_exist(password):
    """
        check if the number exist in password
    """
    for c in password:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password):
    """
        check if the letter exist in password
    """
    for c in password:
        if c.isalpha():
            return True
    return False


def main():
    """
        main function
    """
    password_str = input('please input your password:')

    strength_level = 0

    # rule1: the password length no less than 8
    if len(password_str) >= 8:
        strength_level += 1
    else:
        print('the password length should be no less than 8')

    # rule2: the password should include number
    if check_number_exist(password_str):
        strength_level += 1
    else:
        print('the password length should include number')

    # rule3: the password should include letter
    if check_letter_exist(password_str):
        strength_level += 1
    else:
        print('the password length should include letter')

    if strength_level == 3:
        print('the password is OK!')
    else:
        print('the password is not OK!')


if __name__ == '__main__':
    main()

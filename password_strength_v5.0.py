"""
    Author: Xavier
    Date: 2017/10/10
    Function: check the password strength
    Version: 5.0 package the password function to a class
"""


class PasswordTool:
    """
        password tool class
    """
    def __init__(self, password):
        # property of the class
        self.password = password
        self.strength_level = 0

    # methods of the class
    def password_process(self):
        """
            process the password strength
        """
        # rule1: the password length no less than 8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('the password length should be no less than 8')

        # rule2: the password should include number
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('the password length should include number')

        # rule3: the password should include letter
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('the password length should include letter')

    def check_number_exist(self):
        """
            check if the number exist in password
        """
        has_numeric = False
        for c in self.password:
            if c.isnumeric():
                has_numeric = True
                break
        return has_numeric

    def check_letter_exist(self):
        """
            check if the letter exist in password
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


def main():
    """
        main function
    """
    try_times = 5

    while try_times > 0:

        password_str = input('please input your password:')

        # instance(object) of the PasswordTool class
        password_tool = PasswordTool(password_str)
        password_tool.password_process()

        if password_tool.strength_level == 0:
            strength_str = 'weak'
        elif password_tool.strength_level == 1:
            strength_str = 'relatively weak'
        elif password_tool.strength_level == 2:
            strength_str = 'relatively strong'
        else:
            strength_str = 'strong'

        f = open('password_v5.0.txt', 'a')
        f.write('password: {} strength: {}\n'.format(password_str, strength_str))
        f.close()

        if password_tool.strength_level == 3:
            print('the password is OK!')
            break
        else:
            print('the password is not OK!')
            try_times -= 1
            
        print()

    if try_times <= 0:
        print('too many tries!!!')


if __name__ == '__main__':
    main()

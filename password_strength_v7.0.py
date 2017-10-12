"""
    Author: Xavier
    Date: 2017/10/10
    Function: check the password strength
    Version: 7.0 add more conditions to check password strength level
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

        # rule4: the password should include upper case
        if self.check_upper_exist():
            self.strength_level += 1
        else:
            print('the password length should include upper case')

        # rule5: the password should include lower case
        if self.check_lower_exist():
            self.strength_level += 1
        else:
            print('the password length should include lower case')

        # rule6: the password should include '+ _ *'
        if self.check_character_exist():
            self.strength_level += 1
        else:
            print("the password length should include '+ _ *'")

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

    def check_upper_exist(self):
        """
            check if upper case exists in password
        """
        has_upper = False
        for c in self.password:
            if c.isupper():
                has_upper = True
                break
        return has_upper

    def check_lower_exist(self):
        """
            check if upper case exists in password
        """
        has_lower = False
        for c in self.password:
            if c.islower():
                has_lower = True
                break
        return has_lower

    def check_character_exist(self):
        """
            check if + or _ or * exists in password
        """
        has_character = False
        if '+' in self.password or '_' in self.password or '*' in self.password:
            has_character = True
        return has_character


class FileTool:
    """
        file tool class
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        main function
    """
    try_times = 5
    filepath = 'password_v6.0.txt'

    # call the FileTool class
    file_tool = FileTool(filepath)

    while try_times > 0:

        password_str = input('please input your password:')

        # instance(object) of the PasswordTool class
        password_tool = PasswordTool(password_str)
        password_tool.password_process()

        line = 'password: {} strength: {}\n'.format(password_str, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 6:
            print('the password is OK!')
            break
        else:
            print('the password is not OK!')
            try_times -= 1
            
        print()

    if try_times <= 0:
        print('too many tries!!!')

    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()

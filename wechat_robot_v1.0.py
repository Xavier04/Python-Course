"""
    Author: Xavier
    Date: 2017/9/29
    Function: Wechat robot to classify and match the different language learners
    Version: 1.0 the basic interface
"""

database_name = []          # database to store the Wechat name
database_know = []          # database to store the language know
database_learn = []         # database to store the language learn
language_list = ['Chinese', 'English', 'Russian', 'Japanese', 'Korean']


def robot():
    """
        robot interface
    """
    # print the greet
    print('Hello, it\'s Five Meters! Welcome to join us!')

    # choose the language you know
    language_know = input('Please choose a language you are best at(input the index):\
       \n1 {}\n2 {}\n3 {}\n4 {}\n5 {}'.format(language_list[0],
                                              language_list[1],
                                              language_list[2],
                                              language_list[3],
                                              language_list[4], ))

    # choose the language you want to learn
    language_learn = input('Please choose a language you want to learn or improve(input the index):\
       \n1 {}\n2 {}\n3 {}\n4 {}\n5 {}'.format(language_list[0],
                                              language_list[1],
                                              language_list[2],
                                              language_list[3],
                                              language_list[4], ))
    return language_know, language_learn


def main():
    """
        main function
    """

    global database_name
    global database_know
    global database_learn

    # get the Wechat name
    Wechat_name = input('get the name from Wechat:')

    try:
        # call the robot
        language_know, language_learn = robot()

        # print the choose result
        print('You are good at {}, and you want to learn {}'.format(language_list[int(language_know) - 1],
                                                                    language_list[int(language_learn) - 1]))

        # store the Wechat name
        database_name.append(Wechat_name)

        # store the language the user know
        database_know.append(language_know)

        # store the language the user want to learn
        database_learn.append(language_learn)

    except ValueError:
        print('Please input the index number')
    except:
        print('Please input the right number')

    # print the database to debug
    print()
    print(database_name)
    print(database_know)
    print(database_learn)

    main()


if __name__ == "__main__":
    main()



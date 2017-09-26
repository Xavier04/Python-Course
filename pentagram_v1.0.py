"""
    作者：Xavier
    功能：五角星绘制
    版本：1.0
    日期：17/09/24
"""

import turtle


def main():
    """
        main function
    """
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.exitonclick()
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()



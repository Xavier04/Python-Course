"""
    作者：Xavier
    功能：不同大小的五角星绘制
    版本：2.0
    日期：17/09/27
"""

import turtle


def draw_pentagram(size):
    """
        draw_pentagram
    """
    count = 1
    while count <= 5:
        # turtle.right(144)
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
        main function
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('purple')

    # turtle.right(77)

    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()


if __name__ == '__main__':
    main()



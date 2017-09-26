"""
    作者：Xavier
    功能：用迭代函数绘制不同大小的五角星
    版本：3.0
    日期：17/09/27
"""

import turtle


def draw_recursive_pentagram(size):
    """
        draw_pentagram
    """

    count = 1
    while count <= 5:
        # turtle.right(144)
        turtle.forward(size)
        turtle.right(144)
        count += 1
    # 绘制完一个五角星，更新参数
    size += 10
    turtle.right(36)
    if size <= 200:
        draw_recursive_pentagram(size)


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
    draw_recursive_pentagram(size)

    turtle.exitonclick()


if __name__ == '__main__':
    main()



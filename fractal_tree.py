"""
    作者：Xavier
    功能：用递归函数绘制分形树
    版本：1.0
    日期：17/09/24
"""

import turtle


def draw_branch(branch_length):
    """
        draw fractal tree
    """
    if branch_length > 5:
        # draw the right branch
        turtle.forward(branch_length)
        print('forward', branch_length)
        turtle.right(20)
        print('turn right 20')
        draw_branch(branch_length-15)

        # draw the left branch
        turtle.left(40)
        print('turn left 40')
        draw_branch(branch_length-15)

        # go back to the trunk
        turtle.right(20)
        print('turn right 20')
        turtle.backward(branch_length)
        print('backward', branch_length)


def main():
    """
        main function
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(40)
    turtle.exitonclick()


if __name__ == '__main__':
    main()



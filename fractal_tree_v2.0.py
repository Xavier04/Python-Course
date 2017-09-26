"""
    作者：Xavier
    功能：用递归函数绘制分形树
    版本：1.0
    日期：17/09/24
"""

import turtle


def draw_branch(branch_length, pensize):
    """
        draw fractal tree
    """
    if branch_length > 5:
        if branch_length < 30:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
        # draw the right branch
        turtle.pensize(pensize)
        turtle.forward(branch_length)
        print('forward', branch_length)
        turtle.right(20)
        print('turn right 20')
        draw_branch(branch_length - 15, pensize - 1)

        # draw the left branch
        turtle.left(40)
        print('turn left 40')
        draw_branch(branch_length-15, pensize-1)

        # go back to the trunk
        turtle.right(20)
        print('turn right 20')
        turtle.penup()
        turtle.backward(branch_length)
        turtle.pendown()
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
    initial_length = input('input the initial length:')
    draw_branch(eval(initial_length), eval(initial_length) // 15)
    turtle.exitonclick()


if __name__ == '__main__':
    main()



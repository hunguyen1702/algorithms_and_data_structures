import turtle
import random


tut = turtle.Turtle()
s = turtle.Screen()


def set_color(branch_len, t):
    if branch_len >= 25:
        color = "#000000"
    else:
        color = "#ffffff"
    t.color(color)


def fractal_tree(branch_len, thick, t):
    if thick < 2:
        thick = 2
    t.pensize(thick)
    # angle = random.randrange(8, 13, 3)
    angle = 20
    # subtracted_len = random.randrange(6, 13, 2)
    subtracted_len = 10
    if branch_len > 5:
        # set_color(branch_len, t)
        t.forward(branch_len)
        t.right(angle)
        fractal_tree(branch_len - subtracted_len + 5, thick - 0.7, t)
        t.left(angle * 2)
        fractal_tree(branch_len - subtracted_len, thick - 0.7, t)
        t.right(angle)
        # set_color(branch_len, t)
        t.backward(branch_len)


# turtle.bgcolor("#ffffb3")
tut.left(90)
tut.up()
tut.backward(250)
tut.down()
fractal_tree(80, 7.5, tut)
s.exitonclick()

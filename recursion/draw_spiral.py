import turtle


t = turtle.Turtle()
s = turtle.Screen()


def draw_spiral(tut, line_len):
    if line_len > 0:
        tut.forward(line_len)
        tut.right(90)
        draw_spiral(tut, line_len - 5)

draw_spiral(t, 200)
s.exitonclick()


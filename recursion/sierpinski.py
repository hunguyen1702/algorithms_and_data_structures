import turtle


def draw_triangle(points, color, tut):
    tut.fillcolor(color)
    tut.up()
    tut.goto(points[0][0], points[0][1])
    tut.down()
    tut.begin_fill()
    tut.goto(points[1][0], points[1][1])
    tut.goto(points[2][0], points[2][1])
    tut.goto(points[0][0], points[0][1])
    tut.end_fill()


def get_mid_point(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, tut):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    draw_triangle(points, colormap[degree], tut)
    if degree > 0:
        sierpinski([points[0], get_mid_point(points[0], points[1]), get_mid_point(points[0], points[2])]
                   , degree - 1, tut)
        sierpinski([points[1], get_mid_point(points[0], points[1]), get_mid_point(points[1], points[2])]
                   , degree - 1, tut)
        sierpinski([points[2], get_mid_point(points[2], points[1]), get_mid_point(points[0], points[2])]
                   , degree - 1, tut)


def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    points = [[-100,-50],[0,100],[100,-50]]
    sierpinski(points, 3, t)
    s.exitonclick()


main()


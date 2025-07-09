import turtle
import colorsys

def hypnotic_star_spiral():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.speed(0)
    t.pensize(2)
    n = 100  # number of colors
    h = 0

    for i in range(360):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.pencolor(c)
        t.forward(i * 2)
        t.right(59)
        t.forward(i * 2)
        t.right(59)
        h += 1 / n

    t.hideturtle()
    turtle.done()

hypnotic_star_spiral()

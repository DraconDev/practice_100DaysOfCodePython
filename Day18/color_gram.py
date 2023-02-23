import math
import random
import turtle as drawer

import colorgram

turtle = drawer.Turtle()
turtle.shape('turtle')
turtle.color('red')
drawer.colormode(255)


colors = colorgram.extract(
    r'E:\_Drive\_Programming\_Projects\100 days of code Python\100DaysOfCodePython\100DaysOfCodePython\Day18\picture.jpg', 15)

print(colors)


def painting(colors, size):
    turtle.pensize(10)
    turtle.speed(3)
    for i in range(0, size):
        for _ in range(0, size):
            draw_dots()
        if i % 2:
            turtle.left(90)
            draw_dots()
            turtle.left(90)
        else:
            turtle.right(90)
            draw_dots()
            turtle.right(90)


def draw_dots():
    turtle.pencolor(colors[random.randint(0, len(colors)-1)].rgb)
    turtle.forward(1)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


painting(colors, 10)

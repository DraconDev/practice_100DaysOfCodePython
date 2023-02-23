
import math
import random
import turtle as drawer

turtle = drawer.Turtle()
turtle.shape('turtle')
turtle.color('red')
drawer.colormode(255)


colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
              '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
              '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
              '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
              '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
              '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
              '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
              '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
              '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
              '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']


def dotted_line(count):
    for i in range(count):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shapes(angles):
    for i in range(3, angles):
        turtle.pencolor(random.choice(colorArray))
        for j in range(i):
            turtle.forward(100)
            turtle.right(360/i)


def random_walk(steps):
    turtle.pensize(10)
    turtle.speed(10)
    for i in range(0, steps):
        turtle.pencolor((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))
        length = random.randint(0, 3)
        for i in range(0, length):
            turtle.right(90)
        turtle.forward(30)


def spider_graph(tilt):
    turtle.pensize(5)
    turtle.speed(0)
    for i in range(0, math.floor(360/tilt)):
        turtle.pencolor((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))
        detail = 10
        for i in range(0, 360, detail):
            turtle.left(detail)
            turtle.forward(3*detail)
        turtle.left(tilt)

    # dotted_line(10)

    # random_walk(100)


spider_graph(20)

# draw_shapes(8)
# draw_shapes(8)

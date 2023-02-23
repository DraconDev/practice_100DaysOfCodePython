from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()

RIGHT = "right"
LEFT = "left"
TURN_RIGHT = "tl"
TURN_LEFT = "tr"


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def move_right():
    turtle.right(5)
    turtle.forward(10)


def move_left():
    turtle.left(5)
    turtle.forward(10)


def reset():
    turtle.goto(0, 0)
    turtle.clear()


def move_arrow():
    return


screen.listen()
screen.onkeypress(move_forwards, 'Up')
screen.onkeypress(move_backwards, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.onkeypress(reset, 'c')



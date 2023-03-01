
from turtle import Screen, Turtle


# Func
def screen():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.tracer(0)
    screen.exitonclick()

# Another Solution


class Screen_Toggle:
    """docstring for Screen_Toggle."""

    def __init__(self, ):
        super(Screen_Toggle, self).__init__()
        self = Screen()
        self.setup(600, 600)
        self.bgcolor('black')
        self.tracer(2)
        self.exit = self.exitonclick()
        self.listen()

    def screen_off(self, ):
        self.exit()

    def key_listen(self, player):
        self.listen()
        screen.onkey(player.move_up, "Up")
        screen.onkey(player.move_down, "Down")


def middle_line():
    line = Turtle('square')
    line.color('white')
    line.shapesize(30, .2)
    # return line

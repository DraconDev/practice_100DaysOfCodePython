from turtle import Turtle


class Turtle_Player(Turtle):
    """docstring for Turtle_Player."""

    def __init__(self, ):
        super(Turtle_Player, self).__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(0, -270)
        self.setheading(90)

    def move_up(self, ):
        self.sety(self.ycor()+20)


# def turtle2():
#     turtle = Turtle()
#     turtle.shape('turtle')
#     turtle.color('red')
#     turtle.penup()
#     turtle.goto(0, -270)
#     turtle.setheading(90)

#     def move_up():
#         turtle.setheading(90)

#     turtle.move_up = move_up()

#     return turtle

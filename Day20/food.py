import random
from turtle import Turtle, color


class Food(Turtle):
    """docstring for Food."""

    def __init__(self, ):
        super(Food, self).__init__()
        self.shape('circle')
        self.shapesize(stretch_len=.5, stretch_wid=0.5)
        self.penup()
        self.color('white')
        self.speed(0)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.eaten()

    def eaten(self, ):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

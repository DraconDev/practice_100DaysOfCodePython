import time
from turtle import Screen, Turtle, up

MOVE_DISTANCE = 20
SPEED = .3
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

screen = Screen()


class Snake:
    def __init__(self, length):
        self.snake = []
        self.length = length
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(self.length):
            self.add_segment((i*-20, 0))

    def move_snake(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].setpos(self.snake[i-1].pos())
        self.head.forward(MOVE_DISTANCE)
        screen.update()
        time.sleep(SPEED)

    def add_segment(self, coords):
        new_piece = Turtle('square')
        new_piece.color('white')
        new_piece.setpos(coords)
        new_piece.penup()
        new_piece.clear()
        self.snake.append(new_piece)

    def extend(self, ):
        self.add_segment(self.snake[-1].pos())
        pass

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

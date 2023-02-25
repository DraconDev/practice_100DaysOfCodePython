from turtle import Turtle


def make_ball():
    ball = Turtle()
    ball.color('white')
    ball.shape('circle')
    ball.speed(1)
    ball.penup()
    ball.home()
    return ball

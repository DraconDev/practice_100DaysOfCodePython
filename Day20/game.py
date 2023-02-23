
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
running = True
# print(screen.getshapes())

snake = Snake(3)

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


def game():
    while running:
        snake.move_snake()


game()


screen.exitonclick()
# screen.exitonclick()

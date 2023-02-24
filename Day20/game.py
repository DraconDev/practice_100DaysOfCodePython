
from turtle import Screen

from food import Food
from score import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
running = True
# print(screen.getshapes())

snake = Snake(3)
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


def game():
    while running:
        snake.move_snake()
        collision_with_food()
        collisions_with_body()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            collision_with_wall()


def collision_with_food():

    if (snake.head.distance(food) < 15):
        food.eaten()
        scoreboard.increase_score()
        print('nom')
        snake.extend()
    return True


def collision_with_wall():
    global running
    running = False
    scoreboard.game_over()


def collisions_with_body():
    global running
    for item in snake.snake[1:]:
        if snake.head.distance(item) < 10:
            running = False
            scoreboard.game_over()


game()


screen.exitonclick()
# screen.exitonclick()
# screen.exitonclick()

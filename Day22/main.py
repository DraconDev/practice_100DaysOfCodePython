
import math
import time
from turtle import Screen, Turtle

from ball import make_ball
from board import Screen_Toggle, middle_line
from pad import EnemyPad, PlayerPad
from scoreboard import ScoreBoard

starttime = time.time()

# Gamestate
running = True

# Set up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Draw game elements
player = PlayerPad()
enemy = EnemyPad()
middle_line()
scoreboard = ScoreBoard()
ball = make_ball()
screen.update()

# Listen to up & down press
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


def ball_move():
    ball.forward(2)


def game():
    while running:

        goal()
        ai()
        ball_move()
        detect_collision_with_wall()
        detect_collision_with_pad()
        screen.update()


def goal():
    if ball.xcor() > 300:
        scoreboard.update_score_enemy()
        ball.home()
    if ball.xcor() < -300:
        scoreboard.update_score_player()
        ball.home()


def detect_collision_with_pad():

    for item in enemy.pad:
        if ball.distance(item) < 25:
            ball.right(90)
            return

    for item in player.pad:
        if ball.distance(item) < 25:
            ball.setheading(player.pad[2].ycor()+180)
            return


def detect_collision_with_wall():
    # if ball meets with border
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.setheading(360 - ball.heading())


def ai():
    if ball.ycor() > enemy.pad[2].ycor():
        enemy.move_up(3)
    elif ball.ycor() < enemy.pad[2].ycor():
        enemy.move_down(3)
    else:
        pass


game()


# screen = Screen_Toggle()
# screen.key_listen(player)
# screen.screen_off()

# Screen off
screen.exitonclick()

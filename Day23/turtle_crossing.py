# Set up screen
from turtle import Screen

from cars import Cars
from score_board import ScoreBoard
from turtle_class import Turtle_Player, turtle2

# Gamestate
running = True

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Turtle Crossing')
screen.tracer(0)

# Draw game elements
player = Turtle_Player()
# player = turtle2()
score_board = ScoreBoard()
cars = Cars()

# Listen to up & down press
screen.listen()
screen.onkey(player.move_up, "Up")


def detect_collision():
    global running
    for car in cars.cars:
        if player.distance(car) < 30:
            running = False
            score_board.game_over()


def successful_cross():
    if player.ycor() > 280:
        player.sety(-270)
        score_board.increase_score()
        cars.up_difficulty()


while running:
    cars.move_car()
    cars.reset_car()
    detect_collision()
    successful_cross()
    screen.update()

screen.exitonclick()

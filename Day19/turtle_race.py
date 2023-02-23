import random
from turtle import Screen, Turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# turtle = Turtle()
screen = Screen()
screen.setup(1000, 1000)
turtles = []


def make_turtles(amount):
    for i in range(amount):
        new_turtle = Turtle(shape='turtle')
        turtles.append(new_turtle)
    for i in range(amount):
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].speed(10)
        turtles[i].goto(-450, -400+800*i/(amount-1))


user_bet = screen.textinput(title="Make your bet",
                            prompt="Which color turtle will win?")


def race(turtles):
    no_winner = True
    while no_winner:
        for item in turtles:
            item.forward(random.randint(0, 20))
            # print(item.xcor())
            if item.xcor() >= 450:
                turtle_color = item.color()[0]
                print(f"{turtle_color} wins")
                if turtle_color == user_bet:
                    print('You have bet correctly')
                else:
                    print('You have lost your bet')
                no_winner = False


make_turtles(5)
race(turtles)

screen.exitonclick()

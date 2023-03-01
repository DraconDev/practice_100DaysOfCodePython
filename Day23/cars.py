import random
from turtle import Turtle


class Car(Turtle):
    """docstring for Car."""

    def __init__(self, ):
        super(Car, self).__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.color('white')
        self.penup()
        self.setheading(180)


class Cars():
    """docstring for Cars."""

    def __init__(self, ):
        super(Cars, self).__init__()
        self.cars = []
        self.number_of_cars = 60
        self.make_cars()
        self.speed = 2

    def make_cars(self, ):
        for i in range(self.number_of_cars):
            new_car = Car()
            new_car.setpos(random.randint(330, 6600), random.randint(-3, 3)*60)
            self.cars.append(new_car)

    def reset_car(self, ):
        for car in self.cars:
            if car.xcor() < -350:
                car.setx(random.randint(330, 6600))

    def move_car(self, ):
        for car in self.cars:
            car.forward(self.speed)

    def up_difficulty(self, ):
        self.speed += 1

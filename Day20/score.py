from turtle import Turtle


class ScoreBoard(Turtle):
    """docstring for ScoreBoard."""

    def __init__(self, ):
        super(ScoreBoard, self).__init__()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def increase_score(self, ):
        self.score += 1
        self.update_score()

    def update_score(self, ):
        self.clear()
        self.write(f' Your score: {self.score}',
                   align="center", font=("arial", "20"))

    def game_over(self, ):
        self.goto(0, 0)
        self.write(' Game Over',
                   align="center", font=("arial", "40"))
        pass

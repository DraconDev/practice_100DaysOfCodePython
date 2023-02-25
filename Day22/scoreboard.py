from turtle import Turtle


class ScoreBoard(Turtle):
    """Scoreboard"""

    def __init__(self, ):
        super(ScoreBoard, self).__init__()
        self.penup()
        self.setpos(0, 280)
        self.player_score = 0
        self.enemy_score = 0
        self.hideturtle()
        # self.shapesize(2, 2)
        self.color('white')
        self.write_score()

    def update_score_player(self, ):
        self.player_score += 1
        self.clear()
        self.write_score()

    def update_score_enemy(self, ):
        self.enemy_score += 1
        self.clear()
        self.write_score()

    def write_score(self, ):
        self.setpos(140, 280)
        self.write(f"Player score:{self.player_score}",
                   align='center', font={'arial', '40'})
        self.setpos(-140, 280)
        self.write(f"Enemy score:{self.enemy_score}",
                   align='center', font={'arial', '40'})

from turtle import Turtle


class Pad(Turtle):
    """Pong pads"""

    def __init__(self, ):
        super(Pad, self).__init__()
        self.pad = []

    def make_pad(self, x):
        for i in range(5):
            y = -40+i*20
            self.pad.append(self.make_element(x, y))

    def make_element(self, x, y):
        new_piece = Turtle()
        new_piece.penup()
        new_piece.shape('square')
        new_piece.color('white')
        new_piece.shapesize(1, 1)
        new_piece.setpos(x, y)
        return new_piece

    def move_up(self, pixels=30):
        if self.pad[0].ycor() < 190:
            for item in self.pad:
                item.sety(item.ycor()+pixels)

    def move_down(self, pixels=30):
        if self.pad[-1].ycor() > -190:
            for item in self.pad:
                item.sety(item.ycor()-pixels)


class PlayerPad(Pad):
    """Player pad"""

    def __init__(self, ):
        super(PlayerPad, self).__init__()
        self.penup()
        self.make_pad(260)


class EnemyPad(Pad):
    """Enemy pad"""

    def __init__(self, ):
        super(EnemyPad, self).__init__()
        self.penup()
        self.make_pad(-260)

# class EnemyPad(Pad):
#     """Player pad"""

#     def __init__(self, ):
#         super(EnemyPad, self).__init__()
#         self.penup()
#         self.make_pad(-260)

#     def move_up(self, ):
#         if self.pad[0].ycor() < 200:
#             for item in self.pad:
#                 item.sety(item.ycor()+20)

#     def move_down(self, ):
#         if self.pad[-1].ycor() > -200:
#             for item in self.pad:
#                 item.sety(item.ycor()-20)

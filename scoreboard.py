from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setposition(-270, 260)
        self.update_level_board()

    def update_level_board(self):
        self.write(f"Level: {self.level}",font=FONT)

    def increse_level(self):
        self.level += 1
        self.clear()
        self.update_level_board()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
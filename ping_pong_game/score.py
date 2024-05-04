from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial", 36, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(80, 240)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
        self.goto(-80, 240)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

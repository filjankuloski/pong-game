from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.write(f"{self.l_score} - {self.r_score}", False, ALIGNMENT, FONT)

    def increase_rscore(self):
        self.clear()
        self.write(f"{self.l_score} - {self.r_score + 1}", False, ALIGNMENT, FONT)
        self.r_score += 1

    def increase_lscore(self):
        self.clear()
        self.write(f"{self.l_score + 1} - {self.r_score}", False, ALIGNMENT, FONT)
        self.l_score += 1
from turtle import Turtle

SPEED = 30

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5.0, 1.0)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x, y)

    def up(self):
        y = self.ycor() + SPEED
        self.sety(y)

    def down(self):
        y = self.ycor() - SPEED
        self.sety(y)
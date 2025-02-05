from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(37)
        self.y_dir = 1
        self.x_dir = 1
        self.speed = 10

    def move(self):
        x = (self.x_dir * self.speed) + self.xcor()
        y = (self.y_dir * self.speed) + self.ycor()
        self.setx(x)
        self.sety(y)

    def wall_bounce(self):
        self.y_dir *= -1

    def paddle_bounce(self):
        self.x_dir *= -1
        self.speed += 2

    def reset(self):
        self.goto(0, 0)
        self.x_dir *= -1
        self.speed = 10
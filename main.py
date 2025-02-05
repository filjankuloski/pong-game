from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=paddle.up)
screen.onkeypress(key="Down", fun=paddle.down)
screen.onkeypress(key="w", fun=paddle2.up)
screen.onkeypress(key="s", fun=paddle2.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    print(f"{ball.xcor()}, {ball.ycor()}")

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() >= 410:
        ball.reset()
        scoreboard.increase_lscore()
        screen.update()
        time.sleep(1)

    if ball.xcor() <= -410:
        ball.reset()
        scoreboard.increase_rscore()
        screen.update()
        time.sleep(1)

    ball.move()

screen.exitonclick()
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("Green")
screen.title("The Pong Game")
screen.tracer(0)

# create barrier between two side
for i in range(300, -340, -40):
    pos = (0, i)
    bar = Turtle()
    bar.shape("square")
    bar.color("White")
    bar.penup()
    bar.goto(pos)

left_paddle = Paddle((-460, 0))
right_paddle = Paddle((460, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(left_paddle.go_up, "a")
screen.onkeypress(left_paddle.go_down, "z")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() == -280 or ball.ycor() == 290:
        ball.bounce_y()
    # Detect collision with the paddle
    elif ball.distance(right_paddle) < 50 and ball.xcor() == 440:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() == -440:
        ball.bounce_x()

    # Detect right paddle missed
    elif ball.xcor() > 540:
        scoreboard.left_point()
        ball.reset_position()
    # Detect left paddle missed
    elif ball.xcor() < -540:
        scoreboard.right_point()
        ball.reset_position()


screen.exitonclick()

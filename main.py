from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600, startx=350, starty=0)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(ball.bounce_y, "b")

game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move_forward()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.001
    # Detect R Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if speed < 0:
        game_is_on = False
        print("You are a Legend!!!")


screen.exitonclick()

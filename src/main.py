# @packages
from turtle import Screen
import time

# @scripts
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

time_function_done = time.time()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect upper & lower wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect r_paddle miss
    if ball.xcor() > 450:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle miss
    elif ball.xcor() < -450:
        ball.reset_position()
        scoreboard.r_point()

    # Detect collision with paddles
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.xcor() < 370 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.xcor() > -370:
        # Ensure ball bounce only every .25 sec
        if (time_function_done + .25) < time.time():
            time_function_done = time.time()
            ball.bounce_x()

screen.exitonclick()

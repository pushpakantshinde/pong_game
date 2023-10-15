from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("My Ping-Pong Game")
my_screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

game_ball = Ball()

is_game_on = True


while is_game_on:
    time.sleep(game_ball.ball_speed)
    my_screen.update()
    game_ball.move()

    # Detect collision with upper and lower walls
    if (game_ball.ycor() > 280) or (game_ball.ycor() < -280):
        game_ball.bounce_from_horizontal_walls()

    # Detect collision with the paddles
    if (game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 325) or (game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -325):
        game_ball.bounce_from_paddles()

    # Detect when right paddle misses
    if game_ball.xcor() > 380:
        game_ball.reset_position()

    # Detect when left paddle misses
    if game_ball.xcor() < -380:
        game_ball.reset_position()


my_screen.exitonclick()
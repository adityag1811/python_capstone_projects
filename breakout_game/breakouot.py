from turtle import Turtle,Screen
from ball import Ball
from bricks import Bricks
import time
from paddle import Paddle
from scorecard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TOP_WALL = 280
SIDE_WALL = 370
GAME_OVER_Y = -295

PADDLE_COLLISION_DISTANCE = 50
BRICK_COLLISION_DISTANCE = 40

scorecard = Scoreboard()

screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game!")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.move_left,"Left")
screen.onkeypress(paddle.move_right,"Right")

ball = Ball()

bricks= Bricks()

game_on = True

while game_on:
    time.sleep(.05)
    screen.update()
    ball.move()

    if ball.xcor() > SIDE_WALL or ball.xcor() < -SIDE_WALL:
       ball.bounce_x()

# detect collision with the brick and remove the brick

    if bricks.hit_by(ball):
        ball.bounce_y()


    if len(bricks.all_bricks) == 0:
        bricks.hit_by(ball)
        screen.update()
        scorecard.you_win()
        game_on = False

    if ball.ycor() > TOP_WALL:
        ball.bounce_y()

    if (
            ball.distance(paddle) < PADDLE_COLLISION_DISTANCE
            and ball.ycor() < -250
            and ball.y_move < 0):
        ball.bounce_y()

    if ball.ycor() < GAME_OVER_Y:
        scorecard.game_over()
        game_on = False




screen.exitonclick()
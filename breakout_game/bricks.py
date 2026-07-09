from turtle import Turtle
import random

COLORS = ["blue", "purple", "red", "green"]
ROWS = (40,80,120)

BRICK_COLLISION_DISTANCE = 40

class Bricks():
    def __init__(self):
        self.all_bricks = []
        self.new_brick()

    def new_brick(self):
        for row in ROWS:
            left_edge = -400

            while True:
                remaining_space = 400 - left_edge

                valid_lengths = []

                for lengths in range(4,8):
                    if lengths * 20 <= remaining_space:
                        valid_lengths.append(lengths)

                if not valid_lengths:
                    break

                random_length = random.choice(valid_lengths)
                current_x = left_edge + random_length * 20 / 2
                left_edge = current_x + random_length * 20 / 2

                new_brick = Turtle()
                new_brick.shape("square")

                new_color = random.choice(COLORS)
                new_brick.color("white", new_color)
                new_brick.penup()

                new_brick.shapesize(stretch_wid=2, stretch_len=random_length, outline=2)
                new_brick.goto(current_x,280)


                new_y = new_brick.ycor() - row
                new_brick.goto(current_x,new_y)
                self.all_bricks.append(new_brick)





    def hit_by(self,ball_coord):
        for brick in self.all_bricks:
            if ball_coord.distance(brick) < BRICK_COLLISION_DISTANCE:

                brick.hideturtle()
                self.all_bricks.remove(brick)
                return True





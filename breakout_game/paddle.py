from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5,outline=2)
        self.color("white")
        self.goto(0,-275)


    def move_left(self):
        if self.xcor() < -350:
            return
        new_x = self.xcor() - 30
        self.goto(new_x,self.ycor())

    def move_right(self):
        if self.xcor() > 350:
            return
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial", 24, "bold")
        )

    def you_win(self):
        self.goto(0, 0)
        self.write(
            "YOU WIN!",
            align="center",
            font=("Arial", 24, "bold")
        )
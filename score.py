from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

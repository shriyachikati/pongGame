from turtle import Turtle
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position)

    def move_up(self):
        current_x = self.xcor()
        current_y = self.ycor()
        if current_y - 20 < (SCREEN_HEIGHT / 2) - 80:
            self.setposition(current_x, current_y + 20)

    def move_down(self):
        current_x = self.xcor()
        current_y = self.ycor()
        if current_y - 20 > (-SCREEN_HEIGHT / 2) + 50:
            self.setposition(current_x, current_y - 20)
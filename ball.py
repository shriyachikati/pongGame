from turtle import Turtle, Screen
import random

WIDTH = 800
HEIGHT = 600

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.move_speed = 0.1

    def bounce_wall(self):
        self.y_coordinate *= -1

    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + self.x_coordinate, current_y + self.y_coordinate)

    def bounce_paddle(self):
        self.x_coordinate *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.x_coordinate *= -1
        self.move_speed = 0.1

# screen = Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")
# ball = Ball()
#
# screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
player_1 = Score((100, 250))
player_2 = Score((-100, 250))

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=right_paddle.move_down, key='Down')

screen.onkeypress(fun=left_paddle.move_up, key='w')
screen.onkeypress(fun=left_paddle.move_down, key='s')

game_is_on = 'yes'

while game_is_on == 'yes':
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_wall()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    if ball.xcor() > 400:
        ball.refresh()
        player_2.update()

    elif ball.xcor() < -400:
        ball.refresh()
        player_1.update()
screen.exitonclick()
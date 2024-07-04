from turtle import Screen, Turtle
from padlle import Padlle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
# Set the screen
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

padlle_r = Padlle(370, 0)
padlle_l = Padlle(-370, 0)
ball = Ball()
scoreboard = Scoreboard()


go_padlle = True
while go_padlle:
    screen.update()
    sleep(0.01)
    padlle_r.contro_padlle(up="Up", down="Down")
    padlle_l.contro_padlle(up="w", down="s")
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the padlle
    if ball.xcor() > 340 and ball.distance(padlle_r) < 50:
        ball.bounce_x()

    if ball.xcor() < -340 and ball.distance(padlle_l) < 50:
        ball.bounce_x()

    # Detect if padlle_r miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_l()

    # Detect if padlle_l miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_r()

screen.exitonclick()

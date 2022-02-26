from turtle import Screen, Turtle, xcor
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("69")
screen.tracer(0)


ball = Ball()
ball2 = Ball()
ball2.color("red")
x = ((350,0))
y = ((-350,0))



game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    ball2.move()

    #Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    if ball.distance(x) < 50 and ball.xcor() > 320 or ball.distance(y) < 150 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset_position()
    if ball.xcor() < -400:
        ball.reset_position()

    if ball2.ycor() > 150 or ball2.ycor() < -150:
        ball2.bounce_y()
    if ball2.distance(x) < 150 and ball2.xcor() > 320 or ball2.distance(y) < 150 and ball2.ycor() < -320:
        ball2.bounce_x()
    if ball2.xcor() > 400:
        ball2.reset_position()
    if ball2.xcor() < -400:
        ball2.reset_position()
    

    

        


        

screen.exitonclick()
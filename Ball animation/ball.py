from turtle import Turtle
import random 

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.5
        self.y_move = 0.5
        self.move_speed = 0.0001

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.0009

    def reset_position(self):
        x = random.randrange(0,380)
        y = random.randrange(0,380)
        self.goto(x, y)
        self.move_speed = 0.1
        self.bounce_x()
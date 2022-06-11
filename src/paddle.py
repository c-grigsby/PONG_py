# @packages
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, max_y, min_y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.max_y = max_y - 50
        self.min_y = min_y + 50

    def go_up(self):
        if self.ycor() < self.max_y:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > self.min_y:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)

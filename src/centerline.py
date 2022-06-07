# @packages
from turtle import Turtle


class Centerline(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=2.5, stretch_len=.25)
        self.penup()
        self.goto(0, screen_height)

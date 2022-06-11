# @packages
from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-130, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(130, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))
        self.check_winner()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_winner(self):
        if self.l_score == 10:
            time.sleep(1)
            self.l_score = 'Win'
            self.update_scoreboard()
            time.sleep(1)
            self.l_score = 0
            self.r_score = 0
            self.update_scoreboard()
        elif self.r_score == 10:
            time.sleep(1)
            self.r_score = 'Win'
            self.update_scoreboard()
            time.sleep(1)
            self.l_score = 0
            self.r_score = 0
            self.update_scoreboard()

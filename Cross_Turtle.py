from turtle import Turtle
from constants import *
import random as rd

class CrossTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.customizeTurtle()

    def customizeTurtle(self):
        self.color(FG_COLOR)
        self.penup()
        self.shape("turtle")
        self.setposition((0,-HEIGHT//2+20))
        self.setheading(90)
    def reset(self):
        self.setposition((0,-HEIGHT//2+20))


    def move(self):
        self.setposition((self.xcor(),self.ycor()+10))

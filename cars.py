from turtle import Turtle
from constants import *
import random as rd


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.customizeTurtle()
        self.speed_inc = 0
        self.rd_speed = rd.randint(1, 15)

    def customizeTurtle(self):
        self.color(FG_COLOR)
        self.turtlesize(stretch_wid=CAR_H / 20, stretch_len=CAR_W / 20)
        self.penup()
        self.color(self.get_rd_color())
        self.shape("square")

    def set_random_pos(self):
        x0 = rd.randint(WIDTH // 2, WIDTH // 2 + 500)
        y0 = rd.randint(-HEIGHT // 2 + 50, HEIGHT // 2 - 10)
        self.setposition((x0, y0))

    def get_rd_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return tuple([r, g, b])

    def reset(self):
        self.setposition((-self.xcor(), rd.randint(-HEIGHT // 2 + 50, HEIGHT // 2 - 10)))
        self.rd_speed = rd.randint(1, 40)

    def speed_increase(self):
        self.speed_inc += 5

    def move(self):
        self.setposition((self.xcor() - self.rd_speed - self.speed_inc, self.ycor()))

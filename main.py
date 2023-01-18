# logi Imp
## car not move on rest postion of turtlr
## game over and level to be showed above
## road can be made two way
## avoid collision of cars
## Backward move of cars
## after some tim e cars disapear
# code Imp
## collision is not perfect

import time
from screen import TScreen
from cars import Car
from Cross_Turtle import CrossTurtle
from turtle import Turtle, Screen
from constants import *
import random as rd
road = Screen()
road.colormode(255)
custom_road = TScreen(road)
cross_turtle = CrossTurtle()
level = Turtle()
cars = []
for i in range(TOTAL_CARS):
    car = Car()
    car.set_random_pos()
    cars.append(car)

road.listen()
road.onkeypress(cross_turtle.move, "Up")

game_play = True
l = 1
custom_road.show_level(level, l)
while game_play:
    time.sleep(0.1)
    for car in cars:
        car.move()
        if car.xcor() < -WIDTH // 2:
            car.reset()
        if car.distance(cross_turtle) < 15:
            custom_road.show_game_over()
            game_play = False
            break

        if cross_turtle.ycor() + 20 > HEIGHT // 2:
            l += 1
            level.clear()
            for car in cars:
                car.speed_increase()
            custom_road.show_level(level, l)
            cross_turtle.reset()
    road.update()
road.exitonclick()

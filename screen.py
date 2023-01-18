from turtle import Screen, Turtle
from constants import *

class TScreen:
    def __init__(self,screen):
        self.screen = screen
        self.customize()
        self.x = self.screen.window_width() - 20
        self.y = self.screen.window_height() - 20

    def customize(self):
        self.screen.tracer(0)
        self.screen.setup(width=WIDTH, height= HEIGHT)


    def show_level(self, turtle, level):
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition((0, self.y // 2 - 35))
        turtle.color("blue")
        turtle.write(f"Level - {level}", True, align="center", font=('Arial', 16, 'bold'))

    def show_game_over(self):
        turtle=Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition((-30,0))
        turtle.color("red")
        turtle.write(f"Game Over", True, align="center", font=('Arial', 20, 'bold'))
if __name__ == "__main__":
    screen =Screen()
    scr = TScreen(screen)

    scr.screen.update()
    scr.screen.exitonclick()

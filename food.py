from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=.55, stretch_wid=.55)
        self.color("Blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260,260)
        random_y = random.randint(-260,260)
        self.goto(x=random_x, y=random_y)
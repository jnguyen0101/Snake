from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-200, 200)
        ran_y = random.randint(-200, 200)
        self.goto(ran_x, ran_y)

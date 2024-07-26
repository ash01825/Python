from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.change()
        
    def change(self):
           self.goto(random.randint(-250, 250), random.randint(-250, 250))
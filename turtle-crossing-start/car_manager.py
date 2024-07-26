COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import time
import random

class CarManager:
    def __init__(self) -> None:
        self.cars=[]
        self.speed=STARTING_MOVE_DISTANCE
    def make(self):
        r=random.randint(1,6)
        if r==1:
            new_car=Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(280,random.randint(-250,250),)
            self.cars.append(new_car)

    def move(self):
        
        for i in self.cars:
            i.forward(self.speed)          

    def level_up(self):
        self.speed+=MOVE_INCREMENT
        for car in self.cars:
            car.clear()
            car.hideturtle()
        self.cars=[]    
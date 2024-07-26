STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player:
    def __init__(self):
        self.t=Turtle()
        self.t.penup()
        self.t.shape("turtle")
        self.t.color("black")
        self.t.setheading(90)
        self.t.goto(STARTING_POSITION)
    def move_up(self):
        self.t.forward(MOVE_DISTANCE)
    def move_back(self):
        self.t.backward(MOVE_DISTANCE)
    def reset(self):
        self.t.goto(STARTING_POSITION)
    def finish(self):
        return self.t.ycor()>300
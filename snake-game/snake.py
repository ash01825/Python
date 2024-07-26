from turtle import Turtle
START_POS=[(20,0),(0,0),(-20,0)]
class Snake:
    def __init__(self) -> None:
        self.turtle_bod=[]
        self.make()
        self.head=self.turtle_bod[0]
    def make(self):
        for pos in START_POS:
            new_t=Turtle("square")
            new_t.color("white")
            new_t.penup()
            new_t.goto(pos)
            self.turtle_bod.append(new_t)

    def move(self):
        for t in range(len(self.turtle_bod)-1,0,-1):
            x=self.turtle_bod[t-1].xcor()
            y=self.turtle_bod[t-1].ycor()
            self.turtle_bod[t].goto(x,y)
        self.head.forward(20)
    def extend(self):
        new_t=Turtle("square")
        new_t.color("white")
        new_t.penup()
        new_t.goto(self.turtle_bod[-1].position())
        self.turtle_bod.append(new_t)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
        
FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.goto(-200,250)
        self.color("black")
        self.updscr()


    def updscr(self):
        self.write(f"Level: {self.score}",False,"center",FONT)  
    
    
    def incr_sc(self):
        self.score+=1
        self.clear()
        self.updscr() 

    def over(self):
        self.goto(0,0)
        self.write("Game Over", False,"center",FONT)


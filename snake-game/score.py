from turtle import Turtle
class scboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updscr()
    
    
    def updscr(self):
        self.write(f"Score: {self.score}",False,"center",("Arial",24,"normal"))  
    
    
    def incr_sc(self):
        self.score+=1
        self.clear()
        self.updscr() 

    def over(self):
        self.goto(0,0)
        self.write("Game Over", False,"center",("Arial",24,"normal"))     

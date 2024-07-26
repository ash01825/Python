from turtle import Screen
import time
from snake import Snake
from score import scboard
from food import Food
scr=Screen()
scr.setup(600,600)
scr.title("Snake Game")
scr.bgcolor("black")

scr.tracer(0)

snake=Snake()
fd=Food()
sct=scboard()
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.right,"Right")
scr.onkey(snake.left,"Left")
game=True
while game:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(fd)<15:
        fd.change()
        sct.incr_sc()
        snake.extend()
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        game=False
        sct.over()
    for strike in snake.turtle_bod[1:]:
        if snake.head.distance(strike)<10:
            game=False
            sct.over()    


scr.exitonclick()
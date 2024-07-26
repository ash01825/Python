import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
pl=Player()
cr=CarManager()
screen = Screen()
score=Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()
screen.onkey(pl.move_up,"Up")
screen.onkey(pl.move_back,"Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cr.make()
    cr.move()
    if pl.finish():
        pl.reset()
        cr.level_up()
        score.incr_sc()
    for car in cr.cars:
        if car.distance(pl.t)<20:
            game_is_on=False
            score.over()

screen.exitonclick()    
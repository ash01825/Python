###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Screen,Turtle,colormode
colormode(255)
t=Turtle()
t.penup()
t.hideturtle()
t.speed("fastest")

rgb_colors = []
colors = colorgram.extract(r'/Users/ash/Desktop/Python/hirst-painting-start/image.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
for i in range(1,101):
    t.dot(20,random.choice(rgb_colors))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
scr=Screen()
scr.exitonclick()

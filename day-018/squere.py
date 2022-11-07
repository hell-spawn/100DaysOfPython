from turtle import Screen, Turtle
import random


pepe = Turtle()
screen = Screen()
screen.colormode(255)

circle = 360

for i in range(3, 30):
    angle = 360 / i
    print(angle)
    tup = (random.choice(range(0, 255)), random.choice(range(0, 255)),
               random.choice(range(0, 255)))
    pepe.pencolor(tup)
    for _ in range(0, i):
        pepe.forward(120)
        pepe.right(angle)

screen.exitonclick()

from turtle import Turtle, Screen, colormode
import random

spawn = Turtle();
current_screen = Screen()
directions = [0, 90, 180, 270]
colormode(255)

spawn.pensize(15)
for _ in range( 200 ):
    spawn.forward(50)
    spawn.color(random.choice(range(255)), random.choice(range(255)), random.choice(range(255)))
    spawn.setheading(random.choice(directions))

current_screen.exitonclick();




from turtle import Turtle, Screen, colormode
import random

spawn = Turtle();
spawn.speed("fast")
current_screen = Screen()
colormode(255)

for _ in range( 100 ):
    spawn.color(random.choice(range(255)), random.choice(range(255)), random.choice(range(255)))
    spawn.setheading(spawn.heading() + 10)
    spawn.circle(100)

current_screen.exitonclick();



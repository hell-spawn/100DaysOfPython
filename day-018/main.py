#import colorgram

# Extract 6 colors from an image.

#colors = colorgram.extract('image.jpg', 6)
#rgb_colors = []
#
#for color in colors:
#    new_color = (color.rgb.r, color.rgb.g,color.rgb.b)
#    rgb_colors.append(new_color)
#
#
#print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

rgb_colors = [(133, 133, 182), (216, 218, 222), (86, 181, 83), (179, 63, 57), (207, 160, 82), (54, 88, 130)]


spawn = Turtle();
current_screen = Screen()
colormode(255)

spawn.penup()
spawn.left(270)
spawn.forward(250)
spawn.right(90)
spawn.forward(250)
spawn.right(180)

for _ in range(10):
    for _ in range (10):
        color = random.choice(rgb_colors)
        spawn.dot(20, color)
        spawn.penup()
        spawn.forward(50)
    spawn.penup()
    spawn.backward(500)
    spawn.left(90)
    spawn.forward(50)
    spawn.right(90)




current_screen.exitonclick()

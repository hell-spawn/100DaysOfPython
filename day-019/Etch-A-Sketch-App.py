from turtle import Turtle, Screen, clear
import turtle

spawn = Turtle()
screen = Screen()

def moveForward():
    spawn.forward(10)

def moveBackward():
    spawn.backward(10)

def turn_left():
    spawn.left(10)

def turn_right():
    spawn.right(10)

def clean():
    spawn.reset()


screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clean, "c")

screen.listen()

screen.exitonclick()



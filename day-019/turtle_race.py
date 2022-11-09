from turtle import Turtle, Screen, TurtleGraphicsError, shape
import random



screen = Screen()
screen.setup(500, 400)

turtles = []
posY = 150
posX = -230
is_race_on = False
winner :Turtle|None = None

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")
turtles.append(donatello)
michelangelo = Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")
turtles.append(michelangelo)
leonardo = Turtle()
leonardo.shape("turtle")
leonardo.color("blue")
turtles.append(leonardo)
raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")
turtles.append(raphael)

selection = screen.textinput("Make your bet", "Which turtle will win the race? (Donatello, Michelangelo, Leonardo, Raphael)")


counter = 0;
for current_turtle in turtles:
    current_turtle.penup()
    current_turtle.goto(x=posX, y=(posY - (100 * counter) ))
    counter += 1

if selection:
    is_race_on = True

while is_race_on:
    for current_turtle in turtles:
        current_turtle.forward(random.choice(range(1, 10)))
        if(current_turtle.position()[0] >= 230):
            is_race_on = False
            winner = current_turtle
        
if winner:
    if(winner.color()[0] == "red"):
        winner.write("Raphael Winier", True, align="right")
        print(f"The TMNT more faster is: Raphael { 'You win!' if 'Raphael' == selection else 'You lose'  }")
    if(winner.color()[0] == "orange"):
        winner.write("Michelangelo Winier", True, align="right")
        print(f"The TMNT more faster is: Michelangelo { 'You win!' if 'Michelangelo' == selection else 'You lose'  }")
    if(winner.color()[0] == "purple"):
        winner.write("Donatello Winier", True, align="right")
        print(f"The TMNT more faster is: Donatello { 'You win!' if 'Donatello' == selection else 'You lose'  }")
    if(winner.color()[0] == "blue"):
        winner.write("Leonardo Winier", True, align="right")
        print(f"The TMNT more faster is: Leonardo { 'You win!' if 'Leonardo' == selection else 'You lose'  }")
else:
    print("ERROR")

screen.exitonclick()

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

starting_y = -55
gap = 20

all_turtles = []

for i in range(len(colors)):
    new_racing_turtle = Turtle(shape="turtle")
    new_racing_turtle.fillcolor(colors[i])
    new_racing_turtle.penup()
    new_racing_turtle.goto(x=-230, y=starting_y + i * gap)
    all_turtles.append(new_racing_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.fillcolor()
            if winner == bet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

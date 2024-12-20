from turtle import Turtle, Screen
import random

screen = Screen()


screen.setup(900, 350)
start_y = 150
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
i = 0
list_of_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for _ in range (0, 6):
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(colors[i])
    t.goto(-400, start_y)
    start_y -= 50
    i += 1
    list_of_turtles.append(t)

race_on = False

winner = ""

if user_bet:
    race_on = True

while race_on:
    for t in list_of_turtles:
        if t.xcor() > 425:
            winner = t.pencolor()
            if user_bet.lower() == winner:
                print(f"You've won! The winning color is {winner}!")
            else:
                print(f"You've lost. The winning color is {winner}!")
            race_on = False



        rand_distance = random.randint(0, 20)
        t.forward(rand_distance)


























screen.exitonclick()
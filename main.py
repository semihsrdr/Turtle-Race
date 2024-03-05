import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.bgcolor("black")

colors = ["yellow", "red", "purple", "green", "blue"]
yellow_turtle = Turtle()
red_turtle = Turtle()
purple_turtle = Turtle()
green_turtle = Turtle()
blue_turtle = Turtle()

turtles = [yellow_turtle, red_turtle, purple_turtle, green_turtle, blue_turtle]

for i in turtles:
    i.hideturtle()

starting_x = -450
starting_y = -100
for i in range(len(turtles)):
    turtles[i].shapesize(1.5, 1.5, 1.5)
    turtles[i].pensize(3)
    turtles[i].showturtle()
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].shape("turtle")
    turtles[i].speed("slow")
    turtles[i].goto(starting_x, starting_y)
    starting_y += 50

user_bet = my_screen.textinput(title="Make your bet!",prompt="Which turtle win the race?")


finish_x = 450
game_on = True
while game_on:
    for i in range(len(turtles)):
        random_walk = random.randint(2, 20)
        turtles[i].forward(random_walk)
        if turtles[i].xcor() >= finish_x:
            print(f"{colors[i]} turtle is won")
            if user_bet==colors[i]:
                print("Your bet is won")
            else:
                print("Your bet is lost")
            game_on = False

my_screen.exitonclick()
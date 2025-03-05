from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=700, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "grey", "green", "blue", "purple"]
#created y positions list as the y position is different for each turtle.
y_positions = [-100, -60, -20, 20, 60, 100]
#Every single time we create a new turtle we are appending that new turtle to this empty list.
all_turtles = []
#I created a for loop for the number of turtles we have in the game
for turtle_line in range(0, 6):
#I changed the turtle name from to new_turtles because every single iteration will create a new turtle.
    new_turtles = Turtle()
    new_turtles.shape("turtle")
    new_turtles.penup()
    new_turtles.color(colors[turtle_line])
    new_turtles.goto(x=-340, y= y_positions[turtle_line])
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #checking the end of the screen as if the turtle reached it or not based on the x and y
        if turtle.xcor() > 310:
            #if any of the turtle reaches the end of the screen the race should stop.
            is_race_on = False
            #we used the pencolor function because the pencolor function returns the color of the turtle.
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won the race. The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost the race. The {winning_color} turtle is the winner.")
        random_speed = random.randint(1, 10)
        turtle.forward(random_speed)
screen.exitonclick()
import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.bgcolor("black")
tom = Turtle()
turtle.colormode(255)
direction = [0, 90, 180, 270]
tom.shape("turtle")
tom.color("brown", "green")
tom.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)   #So here's our tuple created,and this is basically our new random color.
    return new_color        # And then this function is going to return that random color as the output.

def check_wall():
    x, y = tom.position()  # Call the method using parentheses and the X and Y are the total screen dimensions
    if abs(x) > 390 or abs(y) > 290: #abs() is used to check if the turtle's position has exceeded the screen boundaries.
        tom.left(180)
        tom.forward(20)
for _ in range(200):
    tom.pencolor(random_color())
    tom.pensize(10)
    tom.forward(30)
    tom.left(random.choice(direction))
    check_wall()

screen.exitonclick()
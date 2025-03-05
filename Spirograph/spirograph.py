import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.bgcolor("white")
tom = Turtle()
turtle.colormode(255)
tom.shape("turtle")
tom.color("brown", "green")
tom.speed(20)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)   #So here's our tuple created,and this is basically our new random color.
    return new_color        # And then this function is going to return that random color as the output.

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(5)
screen.exitonclick()
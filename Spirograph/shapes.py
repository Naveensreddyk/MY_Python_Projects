from turtle import Turtle, Screen
import random
tom = Turtle()
color = ["red", "blue", "green", "orange", "black", "brown", "pink", "yellow", "tan"]
tom.shape("turtle")
tom.color("brown", "green")
tom.speed(10)
angle = 360
side = 3
def draw_shape():
    global side
    for _ in range(side):
        tom.forward(100)
        new_angle = angle / side
        tom.right(new_angle)
    side += 1
    tom.pencolor(random.choice(color))

for _ in range(8):
    draw_shape()

screen = Screen()
screen.exitonclick()
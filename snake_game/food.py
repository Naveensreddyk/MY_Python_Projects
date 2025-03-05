from turtle import Turtle
import random
#created a food class which is inherited from the turtle class
class Food(Turtle):
 #the below is the syntax for the inheritance that we used the super class(turtle)"""
    def __init__(self):
        super(). __init__()
        self.shape("circle")  #we are using the methods from the turtle class.
        self.penup()
        self.color("red")
        self.speed(10)
        self.shapesize(0.6)
        self.spawn_food()
#food will spawn at different location each time. We used the goto method to choose the point of food to be spawned.
    def spawn_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 270)
        self.goto(random_x, random_y)


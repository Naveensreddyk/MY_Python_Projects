from turtle import Turtle
import random
#Created these constants.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []  #Created an empty list for the cars created in the for loop.
        self.car_speed = STARTING_MOVE_DISTANCE #created an attribute for the speed of the car.
    def create_car(self):
#To avoid cars generating rapidly I created a condition from random 1 to 4 everytime the condition picks then only a car gets generated.
        random_chance = random.randint(1, 4)
        if random_chance == 1: #if the random choice is equal to 1 then only the car gets generated.
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250) #car can be generated anywhere in between these co-ordinates.
            new_car.goto(300, random_y) #every newly generated car will go to the complete right side of the screen
            self.all_cars.append(new_car) #All the new cars that are created in the for loop are added to the all_cars list.

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed) #move the turtle backward by distance, opposite to the direction the turtle is headed.


    def level_up(self):
        self.car_speed += MOVE_INCREMENT #everytime time the player reaches the finish line the level increases and speed of the car increases.






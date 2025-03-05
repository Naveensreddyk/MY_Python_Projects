import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()  #created an object screen for the screen class
screen.setup(width=600, height=600)  #set up the screen size.
screen.title("🐢TURTLE CROSS by naveen🐢")
screen.bgcolor("grey")
screen.tracer(0) #It will not show what the turtle is doing until the screen update.

player = Player() #created an object from the player class.
car = CarManager() #created car object from the Car_Manager class.
scoreboard = Scoreboard() #scoreboard object is created form the Scoreboard Class

screen.listen() #This attribute listens to the keystrokes.
screen.onkeypress(player.move_up, "Up" ) #we called a method from the screen class and given the Up key as the key.

game_is_on = True #passed a condition game_is_on = True.
while game_is_on:  #when the condition is true.
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
#collision detection with the cars.
    for cars in car.all_cars:
        if cars.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

#Detect if the player has crossed the road and reached the other side.
    if player.is_player_reached():
        player.go_to_start()
        car.level_up()
        scoreboard.next_level()

screen.exitonclick()

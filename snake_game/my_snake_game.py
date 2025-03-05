from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍SNAKE-GAME by naveen") #title on the screen

"""the turtle will keep moving around and drawing, but you won’t see the drawing happening step-by-step. 
This can make the drawing faster when you're doing a lot of moves because the screen isn’t being updated every time the turtle moves."""
screen.tracer(0)
snake = Snake()  #snake object created from the snake class.
food = Food()    #food object created from the food class.
scoreboard = Scoreboard()  #scoreboard object is created from the Scoreboard class.

screen.listen()   #It listens to the keystrokes.
#I used the on key function to set the keystrokes and called the methods from the snake class.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

#created a while loop, as the game on is true.
while game_on:
#This is like telling the turtle, "Okay, now show me everything on the screen." It updates everything at once.
    screen.update()
    time.sleep(0.1)
    snake.move()  #called the move method from the snake class.

#We are checking if the snake touches the food. We have given here because the turtle is of 20 x 20 pixels.
    if snake.head.distance(food) < 15:
        food.spawn_food()  #If the distance is less than the 15 then the food/turtle randomly appears in a diff loc.
        snake.extend_snake()
        scoreboard.increase_score()  #The increase score method is called from the scoreboard class using the object.
# If the snake head the wall, it wil come out from the exact opposite of the other end.
    if snake.head.xcor() > 290:
        snake.head.goto(-290, snake.head.ycor())
    if snake.head.xcor() < -290:
        snake.head.goto(290, snake.head.ycor())
    if snake.head.ycor() > 290:
        snake.head.goto(snake.head.xcor(), -290)
    if snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), 290)

#wrote a for loop for every part of the snake other than the head.
#It detects the collision with the tail.
    for part in snake.snake[1:]:  #I used the slicing method
        if snake.head.distance(part) < 10:
            scoreboard.game_over()
            snake.reset_snake()

screen.exitonclick()
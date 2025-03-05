from turtle import Turtle

STARTING_POSITION = (0, -280)  #Created the Starting position as the constant as the player will be at the same position every time the game starts or levels up.
MOVE_DISTANCE = 10 #player move distance every time the key up key presses.
FINISH_LINE_Y = 280 #finish line was giving at 280 which the y co-ordinate.


class Player(Turtle):  #Created a Player class which inherits the attributes from the Turtle class.
    def __init__(self):
        super(). __init__()
        self.shape("turtle")
        self.color("brown", "green")
        self.setheading(90)  #given the setheading angle as 90, as it needs to face up.
        self.penup()
        self.go_to_start() #called the go_to_start method which we created.


    def go_to_start(self):
        self.goto(STARTING_POSITION)  #When it called it will go to the starting position.


    def move_up(self):
        self.forward(MOVE_DISTANCE) #created another function for the player to move up everytime presses the key.


    def is_player_reached(self): #Created a method if the player is reached.
        if self.ycor() > FINISH_LINE_Y: #checking the player's y co-ordinate if he reached the finish line.
            return True
        else:
            return False


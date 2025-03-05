from turtle import Turtle
#Created Font As a constant because we are using the same font again and again.
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):  #Created a Scoreboard class and the attributes are inherited from the Turtle class.
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260) #It is displayed at the top left position of the screen according to my given co-ordinates.
        self.next_level() #the next_level method which is return below is called here

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL:{self.level} ", align="left", font= FONT)

#This is displayed in the center of the screen when the game is over.
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME-OVER☠️", align="center", font= FONT)



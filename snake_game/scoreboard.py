import turtle
from snake import Snake
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal" )
#Created a class scoreboard and it is inherited from the Turtle class. So, it can all the things the turtle class can do.
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0   #Initially the score is 0.
        with open("data.txt") as data:  #we opened the data.txt file with a new variable name data
            self.highscore = int(data.read())  #And the data.read reads the file and returns a string value. So, we used int type.
        self.color("white")
        self.penup()
        self.hideturtle()  #It will hide the turtle.
        self.goto(80, 270)
        #write is the method imported form the Turtle class.
        self.write(f"Score:{self.score}    HighScore:{self.highscore}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.clear()  #we use this clear because it will erase the previously written score.
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data: #we opened the data.txt file and changed its mode to write.
                data.write(f"{self.highscore}") #the current highscore is written inside everytime we make a new highscore.
        self.write(f"Score:{self.score}    High Score:{self.highscore}", align= ALIGNMENT, font= FONT)


    def game_over(self):
        self.score = 0
        self.clear()
        self.goto(80, 270)
        self.write(f"Score:{self.score}    HighScore:{self.highscore}", align= ALIGNMENT, font= FONT)












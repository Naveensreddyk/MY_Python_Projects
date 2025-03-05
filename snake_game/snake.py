from turtle import Turtle
#These are the 3 positions for the turtles starting at (0, 0) which at the center(imagine x-axis and y-axis)
#Global Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
#I created the direction as constants because these are the fixed directions for the entire game.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # I created an empty list because we are creating three turtles(squares or snakes).
        self.snake = []
        self.creation_of_snake()
        # Created this head because we use only the 1st square all the time and the remaining
        # squares follow the 1st square.
        self.head = self.snake[0]

    def creation_of_snake(self):
        # created a for loop for the turtles as I am creating 3 and appended the three turtles to the empty list.
        for position in STARTING_POSITIONS:
            self.add_snake(position) #I called the add_snake method here in the for loop.
#created a separate function to create a snake.
    def add_snake(self, position):
        tom = Turtle()
        tom.shape("square")
        tom.color("white")
        tom.penup()
        tom.goto(position)  # I used this goto method which tells the turtle to move to a certain position
        self.snake.append(tom)

    def reset_snake(self):
        for squares in self.snake:
            squares.goto(1000,1000)
        self.snake.clear()
        self.creation_of_snake()
        self.head = self.snake[0]


#To extend the snake at the last position. We write '-1' here as in the lists we can access the last position by writing '-1'.
    def extend_snake(self):
        self.add_snake(self.snake[-1].position()) #here is the position() is the method form the turtle class.

    def move(self):
        # This for loop goes through each part of the snake's body starting from the last part (len(snake) - 1)
        # and moving towards the second part (1).
        # The loop goes backward, moving from the last part to the second one, updating each part's position to follow the one before it.
        for forward in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[forward - 1].xcor()  # snake[forward - 1] gets the part that is right before the current part (forward).
            new_y = self.snake[forward - 1].ycor()  # .xcor() and .ycor() get the x and y coordinates of that previous part.
            self.snake[forward].goto(new_x, new_y)  # This goto method moves the turtle to the specified x and y positions.
        self.head.forward(MOVE_DISTANCE)

#Wrote the functions for the movements of the snake in the game. And passed the angles in the setheading method.
    #It's always the head of the snake(first turtle) which is at position 0 based the head the full snake moves.
    def up(self):
        #if the snake is moving up, then the down stroke not work. And it is similar to all directions below.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random

# Setup screen
screen = Screen()
screen.colormode(255)  # Enables RGB colors to be recognized by the turtle.

# Create turtle
tom = Turtle()
tom.speed("fastest")
tom.penup()  # So it doesn't draw lines
tom.hideturtle()
# List of colors (extracted using colorgram)
color_list = [
    (159, 180, 190), (134, 73, 53), (49, 102, 153), (118, 82, 93),
    (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114),
    (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107),
    (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58),
    (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207),
    (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180),
    (210, 184, 180), (41, 73, 82)
]

# Position turtle to start painting
tom.setheading(225)  # Move diagonally to the left corner
tom.forward(300)
tom.setheading(0)  # Face right

# Function to create dot painting
def dot_paint(rows, cols):
    for row in range(rows):
        for _ in range(cols):
            tom.dot(20, random.choice(color_list))  # Draw a dot
            tom.forward(50)  # Move forward
        tom.setheading(90)  # Turn up
        tom.forward(50)  # Move up
        tom.setheading(180)  # Turn left
        tom.forward(50 * cols)  # Move to the beginning of the row
        tom.setheading(0)  # Face right again

# Call function
dot_paint(10, 10)  # 10 rows, 10 columns

# Keep window open
screen.exitonclick()

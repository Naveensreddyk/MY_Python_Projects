from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(15)
def move_backward():
    tom.backward(15)
def move_counter():
    tom.left(10)
def move_clockwise():
    tom.right(10)
def clear_screen():
    screen.resetscreen()


screen.listen()  #This function activates the event listener. It tells the program to start listening for keyboard inputs.
screen.onkey(move_forward, "w") #This function binds a specific key to a function. When the specified key is pressed, the function gets executed.
screen.onkey(move_backward, "s")
screen.onkey(move_counter, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")



screen.exitonclick()
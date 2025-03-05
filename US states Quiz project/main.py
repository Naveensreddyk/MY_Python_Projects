from turtle import Turtle, Screen
import pandas
import time

# Created an object for the screen class
screen = Screen()
screen.setup(height=491, width=725) #Se-tup the screen according to the dimensions of the picture.
screen.title("🗽U.S. States Guessing Game🗽") #Screen title
screen.bgpic("blank_states_img.gif") #Imported the picture

data = pandas.read_csv("50_states.csv") #Created a variable for the CSV which is read by the pandas module.
all_states = data.state.to_list() #In the CSV file there is a series or Column States and it is converted into list and I gave a variable name to it.

guessed_states = []  #Created an empty list for the UserGuesses if the guess is correct then we will add it in the list.

# Added difficulty selection
difficulty = screen.textinput(title="Choose Difficulty", prompt="Select difficulty: Easy / Medium / Hard").lower()
if difficulty == "easy":
    time_limit = 600  # 10 minutes
elif difficulty == "medium":
    time_limit = 300  # 5 minutes
else:
    time_limit = 180  # 3 minutes

start_time = time.time()  # Start the timer
wrong_guesses = 0  # Counter for wrong guesses
game_running = True  # Flag to control timer

# Timer update function
def update_timer():
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(time_limit - elapsed_time, 0)
    screen.title(f"🗽U.S. States Guessing Game🗽 | Score: {len(guessed_states)}/50 | Time Left: {remaining_time}s")
    if remaining_time > 0:
        screen.ontimer(update_timer, 1000)  # Call this function every second
    else:
        screen.title("Time's Up! Check 'States_To_Learn.csv' to improve.")

# Start the timer update loop
update_timer()

# The while loop will run until the guessed states count or length is 50.
while len(guessed_states) < 50:
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(time_limit - elapsed_time, 0)  # Calculate remaining time

    if remaining_time == 0:
        break  # Stop the game if time runs out

    User_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct | Time Left: {remaining_time}s", prompt="Enter a State Name:").title()

    if User_answer == "Exit": #This is the prompt if the user wants to exit the game.
        remaining_states = [state for state in all_states if state not in guessed_states] #Using List comprehension we created a new list
        new_data = pandas.DataFrame(remaining_states) #We are creating a new data frame for the remaining states.
        new_data.to_csv("States_To_Learn.csv") #And the remaining states are added to a new CSV file.
        break #This will come out of the loop and exits the game.
#If the user guesses wrong 3 times in a row then the hint will be shown on the title area.
    if User_answer not in all_states and User_answer != "Exit":  # If answer is wrong and the user is not exiting the game.
        wrong_guesses += 1 #Then the wrong guesses will be increased.
        if wrong_guesses % 3 == 0:  # Every 3 wrong guesses, give a hint
            hint_state = [state for state in all_states if state not in guessed_states] #This is a list comprehension method for writing a loop in a shorter way.
            if hint_state:
                screen.title(f"Hint: One state starts with '{hint_state[0][0]}' | Time Left: {remaining_time}s")
        continue  # Skip to next iteration

    if User_answer in all_states: #This checks the condition if the user guess is in the all states.
        guessed_states.append(User_answer) #If the user guess is in the all states then the user answer will be added to the guessed states
        tom = Turtle() #created a turtle because when the user guessed correctly, we need a turtle to write the state name.
        tom.hideturtle() #we don't want to see any pointers or turtle on the screen.
        tom.penup() #we don't want to draw lines on the screen. So, the pen is always up.
        correct_state = data[data.state == User_answer] #we are creating a variable for the user answer and state that matches with the user answer in 50_states CSV.
        tom.goto(correct_state.x.item(), correct_state.y.item()) #giving the co-ordinates to the turtle and we used .item() cause the pandas library takes the index number first to skip that.
        tom.write(User_answer) #User answer is written in the co-ordinates if the user answer is in the 50_states CSV.

# If time runs out, show a message
if len(guessed_states) < 50:
    screen.title("Time's Up! Check 'States_To_Learn.csv' to improve.")

screen.mainloop()  # Keep the turtle graphics window open

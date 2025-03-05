#imported all the modules from the tkinter module
from tkinter import *
#defined a class to perform the calculation to convert miles to kms.
def miles_to_kms():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")
#created an object called window from the Tkinter class.
window = Tk()
window.title("MILES TO KILOMETER CONVERTER") #Given a title to display on the title bar of the window.
window.config(padx=40, pady=40) #Given the configurations for the window basically the window dimensions padX is x-axis and padY is y-axis.

miles_input = Entry(width=9) #Created an object from the Entry class, which basically import an entry box.
miles_input.grid(column=1, row= 0) #This method is called the grid method done by assuming the window as a grid.

miles_label = Label(text="Miles") #Created a label from the Label class
miles_label.grid(column=2, row= 0) #placed exactly beside the miles entry box.

is_equal_label = Label(text="Is Equal To")
is_equal_label.grid(column=0, row= 1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row= 1)

kilometer_label = Label(text="Kms")
kilometer_label.grid(column=2, row= 1)

#Created an object from the Button class and given a command to it if we press the button and as a command the function is passed.
calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(column=1, row= 2)
#This is the window main loop which keeps the window open
window.mainloop()
from  tkinter import *
window = Tk() #Created an object window from the tkinter class.
window.title("My first GUI program") #same as screen.title() in turtle graphics. Here window.title().
window.minsize(width=500, height= 300) #Given the dimensions of the window or screen.
#we created a my_label variable ang given a label to the screen by calling Label method. And it can also take font.
my_label = Label(text="I am Naveen", font=("Arial", 24, "bold"))
my_label.pack()  #'pack()' will get hold of my_label and place it in the middle of the screen.

#Creating a button and make it interactive.

def button_clicked():
    new_text = input.get()
    my_label["text"]= new_text

button = Button(text="click me", command= button_clicked)
button.pack()

#Entry like we can give input

input = Entry(width= 10) #It will create a Entry box in the screen and we can enter anything.
input.pack() #it will make sure the entry is visible on the screen.
input.get() #It will get the text we entered in the entry box.


window.mainloop()
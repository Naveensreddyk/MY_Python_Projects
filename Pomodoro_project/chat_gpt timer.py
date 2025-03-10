from tkinter import *
import math
import pygame  # Use pygame for playing custom sound effects
import winsound
# Initialize pygame mixer for sound
pygame.mixer.init()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "None"

#------------------------------WINDOW POP-UP------------------------------#
def raise_window(window):
    window.attributes('-topmost', 1)
    window.after(100, lambda: window.attributes('-topmost', 0))

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pygame.mixer.music.stop()
    start_button.config(state='normal')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Tick-Tock", fg=GREEN, bg=YELLOW)
    check_marks.config(text="")
    global reps
    reps = 0
    # Play reset sound
    winsound.Beep(500, 300)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state='disabled')
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Recharge-Mode", fg=RED, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
        # Play long break sound
        winsound.Beep(500, 300)
        pygame.mixer.music.load("long_break_sound.mp3")  # Replace with your own sound
        pygame.mixer.music.play()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Snack-Time", fg=PINK, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
        # Play short break sound
        winsound.Beep(500, 300)
        pygame.mixer.music.load("nature.mp3")  # Replace with your own sound
        pygame.mixer.music.play()
    else:
        count_down(work_sec)
        timer_label.config(text="Task-Mode", fg="black", bg=YELLOW, font=(FONT_NAME, 28, "bold"))
        # Play work session sound
        pygame.mixer.music.load("ticking_clock.wav")  # Replace with your own sound
        pygame.mixer.music.play()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        raise_window(window)
        start_timer()
        mark = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔️"
        check_marks.config(text=mark)
        # Play cycle end sound (successful end of a cycle)
        pygame.mixer.music.load("cycle_end_sound.mp3")  # Replace with your own sound
        pygame.mixer.music.play()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("CHOP-TIMER")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Timer Label
timer_label = Label(text="Tick-Tock", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
timer_label.grid(column=1, row=0)

# Create Canvas for Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)  # Keep the image center aligned
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Create Start Button
start_button = Button(text="Start", bg=YELLOW, fg="black", font=("Arial", 14, "bold"), relief="ridge", borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)

# Create Reset Button
reset_button = Button(text="Reset", bg=YELLOW, fg="black", font=("Arial", 14, "bold"), relief="ridge", borderwidth=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Create Check Marks Label
check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()

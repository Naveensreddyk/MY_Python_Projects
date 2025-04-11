from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- STYLING VARIABLES ------------------------------- #
BG_COLOR = "#f5f5f5"  # Light neutral background
FONT_NAME = "Segoe UI"
BUTTON_FONT = (FONT_NAME, 10, "bold")
button_bg = "#4a90e2"  # Soft blue button
button_fg = "white"
hover_bg = "#357ABD"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = (
            [random.choice(letters) for _ in range(random.randint(8, 10))] +
            [random.choice(symbols) for _ in range(random.randint(2, 4))] +
            [random.choice(numbers) for _ in range(random.randint(2, 4))]
    )

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check for empty fields and highlight them
    if not website:
        website_entry.config(bg="#ffcccc")
    else:
        website_entry.config(bg="white")

    if not email:
        email_entry.config(bg="#ffcccc")
    else:
        email_entry.config(bg="white")

    if not password:
        password_entry.config(bg="#ffcccc")
    else:
        password_entry.config(bg="white")

    # If any field is empty, show a warning and return
    if not website or not email or not password:
        messagebox.showwarning(title="Warning!", message="Please fill in all the fields before saving.")
        return

    try:
        with open("MyPasswords.json", "r") as passwords_data:
            data = json.load(passwords_data)
    except (FileNotFoundError, json.JSONDecodeError):
        data = new_data
    else:
        data.update(new_data)
    finally:
        with open("MyPasswords.json", "w") as passwords_data:
            json.dump(data, passwords_data, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        messagebox.showinfo(title="Success", message="Password added successfully!")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().strip()

    if not website:
        messagebox.showwarning(title="Warning!", message="Please enter a website to search.")
        return

    try:
        with open("MyPasswords.json") as passwords_data:
            data = json.load(passwords_data)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="❌ No Data File Found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="ERROR", message="❌ Data file is empty or corrupt.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details found for '{website}'.")


# ---------------------------- CLEAR FIELDS ------------------------------- #
def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "naveensreddyk@gmail.com")
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)
# Canvas with Logo
canvas = Canvas(height=200, width=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:", bg=BG_COLOR, font=(FONT_NAME, 10)).grid(row=1, column=0)
Label(text="Email/Username:", bg=BG_COLOR, font=(FONT_NAME, 10)).grid(row=2, column=0)
Label(text="Password:", bg=BG_COLOR, font=(FONT_NAME, 10)).grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_gen, font=BUTTON_FONT, bg=button_bg,
                                  fg=button_fg, activebackground=hover_bg)
generate_password_button.grid(row=3, column=3)

search_button = Button(text="Search", command=search_password, font=BUTTON_FONT, bg=button_bg,
                       fg=button_fg, activebackground=hover_bg)
search_button.grid(row=1, column=3)

# Button Frame for Add and Clear
button_frame = Frame(bg=BG_COLOR)
button_frame.grid(row=4, column=1, columnspan=2, pady=10)

add_button = Button(button_frame, text="Add", width=10, command=save, font=BUTTON_FONT, bg=button_bg,
                    fg=button_fg, activebackground=hover_bg)
add_button.pack(side=LEFT, padx=5)

clear_button = Button(button_frame, text="Clear", width=10, command=clear_fields, font=BUTTON_FONT,
                      bg=button_bg, fg=button_fg, activebackground=hover_bg)
clear_button.pack(side=RIGHT, padx=5)

window.mainloop()

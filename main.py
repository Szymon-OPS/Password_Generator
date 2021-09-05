from tkinter import *
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ----------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # LIST Comprehension version with methods imported from random module
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    # Merge all password characters using join() method
    password = "".join(password_list)
    password_entry.insert(0, string=password)
    # Automatically copy generated password using pyperclip package
    pyperclip.copy(password)

# ---------------------------- UI SETUP --------------------------------
window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)
window.config(padx=50, pady=50)

# Canvas object to add color/picture overlapping layers on screen
canvas = Canvas(height=200, width=200)

# Add logo on canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS

## Website
website_lab = Label(text="Website:")
website_lab.grid(column=0, row=1)
## Email/Username
email_lab = Label(text="Email/Username:")
email_lab.grid(column=0, row=2)
## Password
password_lab = Label(text="Password:")
password_lab.grid(column=0, row=3)

# ENTRIES

## Website entry
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

## Email/Username entry
email_entry = Entry(width=36)
# add text to begin with
email_entry.insert(0, string="your@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

## Password entry
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# BUTTONS

## Calls generate_password() when pressed
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

## Add - will save password when pressed
add_button = Button(width=37, text="Add")
add_button.grid(column=1, row=4, columnspan=2)

## Search - will find password when pressed
search_button = Button(text="Search", width=13)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()

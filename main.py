from tkinter import *

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

## Generate Password - will generate password when pressed
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

## Add - will save password when pressed
add_button = Button(width=37, text="Add")
add_button.grid(column=1, row=4, columnspan=2)

## Search - will find password when pressed
search_button = Button(text="Search", width=13)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()

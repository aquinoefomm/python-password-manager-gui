from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    gen_password = ''.join(password_list)

    password_entry.insert(END, gen_password)

# --------------------------- SEARCH JSON FILE ----------------------------- #

def search():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title="Warning!", message='Fill up a website to search.')
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Warning!", message="No data file found!")
        else:
            website_list = []
            for key in data:
                website_list.append(key)
            if website_entry.get() in website_list:
                messagebox.showinfo(message=f"Email:{data[website_entry.get()]['email']} \n "
                                            f"Password:{data[website_entry.get()]['password']}")
            else:
                messagebox.showwarning(message=f'{website_entry.get()} not found :(')
    website_entry.delete(0, END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Funcion must create a file called data.txt
def save():

    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message='Fill up of fields and try again.')
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old with new data:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries:
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "aquinoefomm@hotmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons:
search_button = Button(text="Search", width=10, highlightthickness=0, command=search)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", width=10, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
from random import randint
import pyperclip
import datetime
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    website_box = website_entry.get()
    email_box = username_entry.get()
    if len(website_box) == 0 or len(email_box) == 0:
        messagebox.showwarning(title="Warning!", message="Please make sure you have entered "
                                                         "a website and email/username.")
    else:
        random_letters = [random.choice(letters) for _ in range(randint(8, 10))]
        random_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]
        random_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]
        password_list = random_letters + random_symbols + random_numbers

        random.shuffle(password_list)

        password = "".join(password_list)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    current_date = datetime.datetime.now()
    formatted_date = current_date.isoformat()
    json_datetime = json.dumps(formatted_date)
    new_data = {
        website:
            {"Username/Email": email,
             "Password": password,
             "Created Date": json_datetime}
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Warning!", message="Please make sure you haven't left any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"Here is your login data:\n\nWebsite: {website} "
                                                 f"\nEmail: {email} \n Password: {password} "
                                                 f"\n\nIs it Ok to save?")
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- Search Password ------------------------------- #


def find_password():
    website_entry_key = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
        try:
            email = data[website_entry_key]["Username/Email"]
            password = data[website_entry_key]["Password"]
            messagebox.showinfo(title=f"{website_entry_key}", message=f"Login data of {website_entry_key} are:"
                                                                      f"\n\nEmail: {email}\nPassword: {password}\n\n"
                                                                      f"The password has been copied to the clipboard,"
                                                                      f" so that you can paste it to log in to your "
                                                                      f"account..")
            pyperclip.copy(password)

        except KeyError:
            messagebox.showwarning(title="Warning!", message=f"No details for the '{website_entry_key}' exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website/Account:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "email@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", width=14, bg="white", command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Save to Database", width=43, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

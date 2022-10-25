from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import *


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    Password_entry.delete(0, END)
    Password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_data = {website_entry.get(): {"email": Email_entry.get(), "password": Password_entry.get()}}
    if website_entry.get() == "" or Password_entry.get() == "":
        messagebox.showinfo(title="Attention", message="You must fill all!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \nEmail:{Email_entry.get()}"
                                               f"\nPassword:{Password_entry.get()} \nIs ok to save?")
        if is_ok:
            try:
                file = open("./password.json", mode="r")
                data = json.load(file)
                data.update(new_data)
                file.close()
            except:
                with open("./password.json", mode="w") as ps:
                    json.dump(new_data, ps, indent=4)

            else:
                with open("./password.json", mode="w") as ps:
                    json.dump(data, ps, indent=4)
            finally:
                website_entry.delete(0, END)
                Password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    try:
        file = open("password.json")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning!", message=f"{FileNotFoundError}")
        file.close()
    else:
        try:
            data = json.load(file)
            new_data = data[website_entry.get()]
            email = new_data["email"]
            password = new_data["password"]
        except:
            messagebox.showinfo(title="Warning!", message="No Website Founded")
        else:
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"email: {email}\npassword: {password}")
    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, )
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=W)
Email_label = Label(text="Email/Username:")
Email_label.grid(row=2, column=0, sticky=W)
Password_label = Label(text="Password:")
Password_label.grid(row=3, column=0, sticky=W)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()
Email_entry = Entry(width=60)
Email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
Email_entry.insert(0, "choud@systena.co.jp")
Password_entry = Entry(width=40)
Password_entry.grid(row=3, column=1, sticky=W)
website_button = Button(text="Search", width=16, command=find_password)
website_button.grid(row=1, column=2, )
Password_button = Button(text="Generate Password", width=16, command=generate_password)
Password_button.grid(row=3, column=2, )

add_button = Button(text="Add", width=51, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()

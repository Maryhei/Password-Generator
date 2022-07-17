# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def search():
    Website = Website_entry.get()
    try:
        with open("data.json", "r") as data:
            content = json.load(data)
    except:
        messagebox.showinfo(title="Error", message="Sorry, No info")
    else:
        if Website in content:
            email = content[Website]["email"]
            password = content[Website]["password"]
            messagebox.showinfo(title=Website, message=f"Email: {email}\n"
                                                       f"Password: {password} ")

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    Password_entry.delete(0, END)
    Password_entry.insert(index=0, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_value():
    Website = Website_entry.get()
    Username = Username_entry.get()
    Password = Password_entry.get()
    new_data = {
        Website: {
            "email": Username,
            "password": Password,
        }
    }
    if len(Website) != 0 and len(Username) != 0 and len(Password) != 0:
        is_ok = messagebox.askokcancel(title=Website, message="These are details entered:\n"
                                                      f"Email: {Username}\n"
                                                      f"Password: {Password}\n"
                                                      f"Confirm?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    content = json.load(data)
                    content.update(new_data)

                with open("data.json", "w") as data:
                    json.dump(content, data, indent=4)
                    Website_entry.delete(0, END)
                    Password_entry.delete(0, END)
            except:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            finally:
                Website_entry.delete(0, END)
                Password_entry.delete(0, END)


    elif len(Website) == 0 or len(Username) == 0 or len(Password) == 0:
        messagebox.showinfo(title="Error", message="Please fill in all the blanks")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
window = Tk()
window.config(pady=50, padx=50)
window.title("Password manager")

#CANVAS
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#LABELS
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)

Username_label = Label(text="Email/Username:")
Username_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

#ENTRYS
Website_entry = Entry(width=17)
Website_entry.grid(column=1, row=1)
Website_entry.focus()

Username_entry = Entry(width=35)
Username_entry.grid(column=1, row=2, columnspan=2)
Username_entry.insert(index=0, string="@Your Email@")

Password_entry = Entry(width=17)
Password_entry.grid(column=1, row=3)

#BUTTON
Generate_password = Button(text="Generate Password", command=generate_password)
Generate_password.grid(column=2, row=3)

Add = Button(text="Add",width=33, command=save_value)
Add.grid(column=1, row=4, columnspan=2)

Search = Button(text="Search", width= 14, command=search)
Search.grid(column=2, row=1)


window.mainloop()




import tkinter as tk
from tkinter import PhotoImage, Canvas, END, messagebox
import pandas as pd
import os
import random
import string


def search():
    web = website_entry.get()
    use = username_entry.get()
    if web == "" or use == "":
        messagebox.showinfo(title="Error", message="Please enter the website and password")
    else:
        try:
            data=pd.read_csv("pass_manager_csv")
            entry = data[(data['Website'] == web) & (data['Email/Username'] == use)]
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="File not found")
        else:
            if not entry.empty:
                    found_password = entry.iloc[0]['Password']
                    messagebox.showinfo(title=web,message=f"E-mail: {use}\n Password: {found_password}")
            else:
                messagebox.showerror(title="Error",message="No such details exist")  













def generate():
    password_parts = []

    password_parts.extend(random.choice(string.ascii_letters) for _ in range(random.randint(8,10)))
    password_parts.extend(random.choice(string.digits) for _ in range(random.randint(2, 4)))
    password_parts.extend(random.choice(string.punctuation) for _ in range(random.randint(2, 4)))

    random.shuffle(password_parts)
    
    passwood = ''.join(password_parts)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, passwood)

def save():
    web = website_entry.get()
    use = username_entry.get()
    passo = password_entry.get()
    
    if web == "" or use == "" or passo == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askyesno(title="Save", message="Do you want to save your info?")
        if is_ok:
            new_entry = pd.DataFrame([[web, use, passo]], columns=["Website", "Email/Username", "Password"])
            if not os.path.exists("pass_manager.csv"):
                new_entry.to_csv("pass_manager.csv", index=False)
            else:
                new_entry.to_csv("pass_manager.csv", mode='a', header=False, index=False)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = tk.Label(text="Website")
website.grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

username = tk.Label(text="Email/Username")
username.grid(row=2, column=0)
username_entry = tk.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password = tk.Label(text="Password")
password.grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

pass_gen = tk.Button(text="Generate Password", command=generate)
pass_gen.grid(row=3, column=2)

search_butt=tk.Button(text="Search",command=search,width=13)
search_butt.grid(row=1,column=2)

add = tk.Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()

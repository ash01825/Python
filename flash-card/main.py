import tkinter as tk
import pandas as pd
import random

# Define background color
BACKGROUND_COLOR = "#B1DDC6"
# Create the main window
window = tk.Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
learn_diictionary=[]

try:
    old_words=pd.read_csv(r"data\learn_words.csv")
except FileNotFoundError:
    og_words = pd.read_csv(r"data\spanish_words.csv")
    learn_diictionary=og_words.to_dict(orient="records")
else:
    learn_diictionary=old_words.to_dict(orient="records")

# Load images
card_front = tk.PhotoImage(file=r"images\card_front.png")
card_back = tk.PhotoImage(file=r"images\card_back.png")
right = tk.PhotoImage(file=r"images\right.png")
wrong = tk.PhotoImage(file=r"images\wrong.png")

# Functions
def get_spanish_word():
    
    random_word = random.choice(learn_diictionary)
    return random_word
def learn_word():
    canvas.itemconfig(card_shown,image=card_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=spanish_word["English"],fill="white")

def change_word():
    global spanish_word,timer
    window.after_cancel(timer)
    spanish_word=get_spanish_word()
    canvas.itemconfig(card_shown,image=card_front)
    canvas.itemconfig(title,text="Spanish",fill="black")
    canvas.itemconfig(word,text=spanish_word["Spanish"],fill="black")
    timer=window.after(3500,learn_word)
def done():
    learn_diictionary.remove(spanish_word)
    data=pd.DataFrame(learn_diictionary)
    data.to_csv(r"data\learn_words.csv",index=False)
    change_word()

# Create a canvas and add the image and text
canvas = tk.Canvas(height=526, width=800)
card_shown=canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title=canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"),fill="black")
spanish_word=get_spanish_word()
word=canvas.create_text(400, 263, text=spanish_word["Spanish"], font=("Ariel", 60, "bold"),fill="black")
canvas.grid(row=0, column=0,columnspan=2)

#Create Buttons
cross_button=tk.Button(image=wrong,highlightthickness=0,command=change_word)
cross_button.grid(row=1,column=0)
tick_button=tk.Button(image=right,highlightthickness=0,command=done)
tick_button.grid(row=1,column=1)
# Start the Tkinter event loop
timer=window.after(3500,learn_word)
change_word()
window.mainloop()

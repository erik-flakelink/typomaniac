#HOME ROW
characters_1 = ["f", "j"]
characters_2 = characters_1 + ["d", "k"]
characters_3 = characters_2 + ["s", "l"]
characters_4 = characters_3 + ["a", ";"]

#HOME ROW 2
characters_5 = characters_4 + ["space"]
characters_6 = characters_5 + ["g", "h"]

#UPPER ROW
characters_7 = characters_6 + ["r", "u"]
characters_8 = characters_7 + ["e", "i"]
characters_9 = characters_8 + ["w", "o"]
characters_10 = characters_9 + ["q", "p"]
characters_11 = characters_10 + ["t", "y"]

#LOWER ROW
characters_12 = characters_11 + ["c", "n"]
characters_13 = characters_12 + ["x", "m"]
characters_14 = characters_13 + ["z", ","]
characters_15 = characters_14 + ["v", "b"]


import random
character = random.choice(characters_15)

from tkinter import *

root = Tk()

root.title("TYPOMANIAC")

root.state("zoomed")

Canvas = Canvas(root, width = 974, height = 205, bg="#00f5ff",highlightthickness=0)      
Canvas.pack()
Splash = PhotoImage(file="SPLASH.png")
Canvas.create_image(0,0, anchor=NW, image=Splash)

Char = ("Times New Roman", 200)

Subtitle = ("Times New Roman", 50)

Demo = Label(root, text='!!! Demo !!!',font=Subtitle)
Demo.pack(side=TOP)

Str = Label(root, text=character,font=Char)
Str.pack(side=TOP)

def check(self):
    global character
    root.unbind('<' + character + '>')
    print("CORRECT!")
    Str["text"] = random.choice(characters_15)
    character = Str["text"]
    root.bind('<' + character + '>', check)
        

Input = Entry(root)
Input.config(font=Char)
Input.pack()

root.bind('<' + character + '>', check)

root.mainloop()

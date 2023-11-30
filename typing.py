#HOME ROW
characters_1 = ["f", "j"]
characters_2 = characters_1 + ["d", "k"]
characters_3 = characters_2 + ["s", "l"]
characters_4 = characters_3 + ["a", ";"]

#HOME ROW 2
characters_5 = characters_4 + ["space","space","space","space","space","space","space","space"] 
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

Char = ("Times New Roman", 200)

Subtitle = ("Times New Roman", 50)

Btn = ("Comic Sans MS", 67)

import random

blue = "#8800FF"

diffculty = characters_15

character = random.choice(diffculty)

from tkinter import *


root = Tk()

def root1():
    global root
    root.destroy()
    global blue
    global Canvas2
    global Splash
    global RandomImg
    global Random

    root = Tk()
    root.title("TYPOMANIAC")

    root.configure(background=blue)

    root.state("zoomed")

    Canvas2 = Canvas(root, width = 974, height = 205, bg=blue,highlightthickness=0)      
    Canvas2.pack(anchor=NW)
    Splash = PhotoImage(file="SPLASH.png")
    RandomImg = PhotoImage(file="RANDOM.png")
    Canvas2.create_image(0,0, anchor=NW, image=Splash)

    Random = Button(root, image=RandomImg, compound="left", text="Random", bg=blue, font=Btn, command=root2)
    Random.pack()

    ver = Label(root, text="v0.0.6",font=Subtitle,bg=blue, fg="#000000")
    ver.pack(side=BOTTOM, anchor=SE)
    
    root.mainloop()

def root2():
    global root
    root.destroy()
    global blue
    global Canvas2
    global Splash
    global RandomImg
    global Random

    root = Tk()

    root.title("TYPOMANIAC")

    blue = "#8800FF"

    root.configure(background=blue)

    root.state("zoomed")

    Canvas2 = Canvas(root, width = 974, height = 205, bg=blue,highlightthickness=0)      
    Canvas2.pack(anchor=NW)
    Splash = PhotoImage(file="SPLASH.png")
    RandomImg = PhotoImage(file="RANDOM.png")
    Canvas2.create_image(0,0, anchor=NW, image=Splash)

    Char = ("Times New Roman", 200)

    Subtitle = ("Times New Roman", 50)

    Btn = ("Comic Sans MS", 80)

    global Str
    global multipler
    Str = Label(root, text=character,font=Char,bg=blue, fg="#000000")
    Str.pack()
    multipler = Label(root, text="",font=Subtitle,bg=blue, fg="#000000")
    multipler.pack()
    global multiply
    multiply = 1

    root.bind('<' + character + '>', check)
    
    Canvas3 = Canvas(root, width = 974, height = 205, bg=blue,highlightthickness=0)      
    Canvas3.pack()
    RandomImg = PhotoImage(file="RETURN.png")

    Back = Button(root, image=RandomImg, compound="left", text="Return", bg=blue, font=Btn, command=root1)
    Back.pack()
     
    root.mainloop()

def Random():
    global root
    root.destroy()
    root2()

def check(self):
    global character
    global multiply
    global multiplier
    global blue
    global Str
    global multipler
    character2 = character
    root.unbind('<' + character + '>')
    print("CORRECT!")
    Str["text"] = random.choice(diffculty)
    character = Str["text"]
    if character == character2:
        multiply += 1
        multipler["text"] = "x" + str(multiply)
    else:
        multiply = 1
        multipler["text"] = ""
    root.bind('<' + character + '>', check)

root1()

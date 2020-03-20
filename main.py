import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.title("COLORGAME")
root.geometry("400x400")
root.resizable(False,False)

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown'] 
score = 0
timeLeft = 30
colChoice = None

def start():
    instAndScore.config(text = "\nScore: 0")
    startButton.config(state = DISABLED)
    randColor()
    countdown()

def red():
    global colChoice
    colChoice = 'Red'
    randColor()

def orange():
    global colChoice
    colChoice = 'Orange'
    randColor()

def yellow():
    global colChoice
    colChoice = 'Yellow'
    randColor()

def green():
    global colChoice
    colChoice = 'Green'
    randColor()

def blue():
    global colChoice
    colChoice = 'Blue'
    randColor()

def purple():
    global colChoice
    colChoice = 'Purple'
    randColor()

def pink():
    global colChoice
    colChoice = 'Pink'
    randColor()

def brown():
    colChoice = 'Brown'
    randColor()

def black():
    global colChoice
    colChoice = 'Black'
    randColor()

def white():
    global colChoice
    colChoice = 'White'
    randColor()

def randColor():
    global score
    if colChoice == colours[1]:
        score += 1
        instAndScore.config(text = "\nScore: " + str(score))
    random.shuffle(colours)
    colorLabel.config(fg = str(colours[1]), text = str(colours[0]))

def countdown():
    global score
    global timeLeft
    if timeLeft > -1:
        instAndTime.config(text = "\nTime left: " + str(timeLeft), font = ('Helvetica', 12))
        timeLeft -= 1
        instAndTime.after(1000,countdown)
    elif timeLeft == -1:
        timeLeft = 30
        colorLabel.config(text = "OOOOO", fg = 'black')
        instAndScore.config(text = "\nClick start to play")
        instAndTime.config(text = "\nClick the color based on the text color")
        startButton.config(state = NORMAL)
        messagebox.showinfo("Time's Up!","Your score is {0}".format(score))
        score = 0
def exit():
	qExit = tk.messagebox("do you want to exit?")
	if qExit > 0:
		root.destroy()
		return
instAndScore = Label(root, text = "\nClick start to play", font = ('Helvetica', 12)) 
instAndScore.pack()

colorLabel = Label(root, text = "OOOOO", font = ("Helvetica",60), pady = 40, bg = 'lightgray')
colorLabel.pack(fill = X)

startButton = Button(root,text = "Start!", font = ("algerian",12),command = start)
startButton.pack()

instAndTime = Label(root, text = "\nClick the color based on the text color", font = ('Helvetica',12))
instAndTime.pack()

button1 = Button(root, bg = "red",height = 3, command = red)
button1.pack(side = LEFT, fill = X, expand = TRUE)

button2 = Button(root, bg = "orange",height = 3, command = orange)
button2.pack(side = LEFT,fill = X, expand = TRUE)

button3 = Button(root, bg = "yellow",height = 3, command = yellow)
button3.pack(side = LEFT,fill = X, expand = TRUE)

button4 = Button(root, bg = "green",height = 3, command = green)
button4.pack(side = LEFT,fill = X, expand = TRUE)

button5 = Button(root, bg = "blue",height = 3, command = blue)
button5.pack(side = LEFT,fill = X, expand = TRUE)

button6 = Button(root, bg = "purple",height = 3, command = purple)
button6.pack(side = LEFT,fill = X, expand = TRUE)

button7 = Button(root, bg = "pink",height = 3, command = pink)
button7.pack(side = LEFT,fill = X, expand = TRUE)

button8 = Button(root, bg = "brown",height = 3, command = brown)
button8.pack(side = LEFT,fill = X, expand = TRUE)

button9 = Button(root, bg = "black",height = 3, command = black)
button9.pack(side = LEFT,fill = X, expand = TRUE)

button10 = Button(root, bg = "white",height = 3, command = white)
button10.pack(side = LEFT,fill = X, expand = TRUE)

exit = Button(root, text = "Exit", command = root.destroy)
exit.pack(side = BOTTOM)

root.mainloop()


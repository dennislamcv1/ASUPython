#https://python-course.eu/tkinter/events-and-binds-in-tkinter.php

from tkinter import *
i = 1
j = 1

def function():
    global i
    label = Label(root, text="Welcome ")
    label.grid(row= i, column=0)
    i += 1
    
def function2(event):
    global j
    label = Label(root, text="Python Students!")
    label.grid(row=j, column=1)
    j += 1
    
root = Tk()
root.geometry("300x200")
#Events are controlled by the command function.
button = Button(root, text="Click Here 1", command=function)
button.grid(row=0, column=0)

#Event is triggered by the button.
button2 = Button(root, text="Click Here 2") 
button2.bind('<Button-1>', function2)
button2.grid(row=0, column=1)
root.mainloop()
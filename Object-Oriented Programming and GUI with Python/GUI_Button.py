
from tkinter import *


root = Tk()#Create the root window where all widgets go
root.geometry("400x150")# Set the size of the window
root.title('Buttons')  

def write_message(): #Message for second Button
    print("Welcome to Python!")
def quit(): #Exit the window
       root.destroy()


#Creates the button object with red text
button = Button(root, 
                text="QUIT", 
                fg="red",
                command=root.quit)
button.pack(side=LEFT)
#Creates a second button object that displays a message in console 
message = Button(root,
                 text="Welcome Message",
                 fg="pink",
                 command=write_message)
message.pack(side=RIGHT)

button3 = Button(root, 
                 text="Top", 
                 fg= "green")
button3.pack(side=TOP)

button4 = Button(root, 
                 text="Bottom", 
                 fg= "blue")
button4.pack(side=BOTTOM)
root.mainloop()
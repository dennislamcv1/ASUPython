
from tkinter import *
root = Tk() # Create the root window where all widgets go
# Set the size of the window
root.geometry("700x350")
root.title('Welcome!') #Displays the text at the top of the container.
label1 = Label(root, text="Welcome to GUI's in Python!") # Create a label with words
label2 = Label(root, text = "Python is Amazing!!!", font=("Helvetica", 14)) #Set font and size
label1.config(fg= "green") #Set text color
label1.pack() # Put the label into the window
label2.pack()
root.mainloop() # Start the event loop 
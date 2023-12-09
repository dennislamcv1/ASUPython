#https://www.tutorialspoint.com/python/tk_text.htm
from tkinter import *

root = Tk()
root.geometry("300x300") 
root.title('TextBoxes')  

def insertText():
    user_input=textField1.get("1.0",END)  # read from one text box t1
    textField2.insert(END, user_input) # Add to another text box t2

    
user_input = StringVar() #Declares a string variable.

label1 = Label(root,  text='Enter Your Name', width=15 )  # Creates a label
label1.grid(row=1,column=1) #location on the window

textField1 = Text(root,  height=1, width=16,bg='yellow') # Create a  textbox
textField1.grid(row=1,column=2) #location on the window


b1 = Button(root, text='Update', width=10,bg='red',command=lambda: insertText()) # Creates a button
b1.grid(row=2,column=2) #location on the window

textField2 = Text(root, height=1, width=15, bg='pink' ) # added one textbox to read 
textField2.grid(row=3,column=2) #location on the window


root.mainloop()
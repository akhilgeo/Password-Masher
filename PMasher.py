import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import ImageTk, Image
import os
import pyperclip


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = SecretKey.get()
    return userInput

    


# this is the function called when the button is clicked
def btnClickFunction():


    secretKey = getInputBoxValue()

    medium = var.get() #gets the radio button value
    if medium == 1:
        mString = "facebook"
    elif medium == 2:
        mString = "Twitter"
    elif medium == 3:
        mString = "Linkedin"
    else:
        mString = "Default"


    passwd = (mash(secretKey)+mash(mString))

    Label(root, text=passwd, bg="#FFFF00", font=('arial', 12, 'bold')).place(x=220, y=360)

    Label(root, text="*The generated password has been copied to clipboard", bg="#F0F8FF", font=('arial', 8, 'normal')).place(x=150, y=400)

    pyperclip.copy(passwd)
    spam = pyperclip.paste()
    #getRadioButtonValue()

#replaces the letters in password
def mash(text):
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"&","e":"3","l":"3","o":"^","s":")"," ":"@","u":"+","A":"$","N":"!","T":"#","i":"(","S":"|","B":"?","C":"<","D":";","K":"{"}
    return ''.join(getchar(c) for c in text)
    
   



root = Tk()
#this is the declaration of the variable associated with the radio button group
medium = tk.StringVar()



# This is the section of code which creates the main window
root.geometry('515x426')
root.configure(background='#F0F8FF')
root.title('Password Masher')



# This is the section of code which creates a text input box
SecretKey=Entry(root)
SecretKey.place(x=265, y=119)



img = ImageTk.PhotoImage(Image.open( os.path.dirname(os.path.realpath(__file__))+"\img\logo.png"))
panel = tk.Label(root, image = img, width=120, height=30, bg='#F0F8FF')
panel.place(x=51, y=30)
panel.pack(side = "top", fill = "both")



# This is the section of code which creates the a label
Label(root, text='Your Secret Key', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=119, y=117)



# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#F0F8FF')
frame.place(x=231, y=171)
var = IntVar()
R1 = Radiobutton(frame, text="Facebook", variable=var, value='1', bg='#F0F8FF', font=('arial', 12, 'normal'))                 
R1.pack( anchor = W )

R2 = Radiobutton(frame, text="Twitter", variable=var, value='2', bg='#F0F8FF', font=('arial', 12, 'normal'))               
R2.pack( anchor = W )

R3 = Radiobutton(frame, text="Linkedin", variable=var, value='3', bg='#F0F8FF', font=('arial', 12, 'normal'))
R3.pack( anchor = W)


# This is the section of code which creates a button
Button(root, text='Generate', bg='#E0EEEE', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=230, y=318)





root.mainloop()

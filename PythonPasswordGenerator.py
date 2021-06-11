# Imports
from tkinter import *
from tkinter import messagebox
import random



# Screen in Tkinter
root = Tk()
root.geometry("600x600")
root.title("Python Password Generator")



# Generate Password Function
def GeneratePassword():
    # Delete Previous Text from Entry Box & Get the Length of the Password
    ReturnPassword_Entry.delete(0, END)
    Get_PasswordLength = int(PasswordLength_Entry.get())

    # Create Phrases which the Password Must Be Compromised of:
    LowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    UppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "1234567890"
    Symbols = "!@#$%^&*()<>?"
    
    # Create Password 
    for i in range(0, Get_PasswordLength):
        Password = random.choice(LowercaseLetters + UppercaseLetters + Numbers + Symbols)
        ReturnPassword_Entry.insert(END, Password)



# Copy Password to Clipboard Function
def CopyToClipboard():
    root.clipboard_append(ReturnPassword_Entry.get())
    messagebox.showinfo(title="Password Was Copied to Clipboard", message="Your Password Was Successfully Copied to Your Clipboard")




# Title
Title = Label(root, text="Python Password Generator", font=("Arial", 30))
Title.pack()



# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=60)



# Password Length Label
PasswordLength_Label = Label(MainFrame, text="Password Length:", font=("Arial", 20))
PasswordLength_Label.pack()



# Create an Entry Box for Password Length
PasswordLength_Entry = Entry(MainFrame, font=("Arial", 16))
PasswordLength_Entry.pack()



# Return the Password in Entry Box                 
ReturnPassword_Entry = Entry(MainFrame, font=("Arial", 26), bg="dodgerblue")
ReturnPassword_Entry.pack(pady=36)



# Generate Password Button
GeneratePasswordBtn = Button(MainFrame, text="Generate Password", width=16, height=1, font=("Arial", 14), command=GeneratePassword)
GeneratePasswordBtn.pack()



# Copy Password to Clipboard Button
CopyToClipboardBtn = Button(MainFrame, text="Copy to Clipboard", width=16, height=1, font=("Arial", 14), command=CopyToClipboard) 
CopyToClipboardBtn.pack()



# Mainloop
root.mainloop()

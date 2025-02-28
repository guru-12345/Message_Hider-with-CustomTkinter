#Task 1- Change the background color to "grey"
#Task 2- Change the size of the window to 600x450
#Task 3- Add the tilte of the window to "Message Encoder"

# Importing libraries we need
import customtkinter as ctk   # A library to make cool and modern windows
from PIL import Image, ImageTk    # A library to work with pictures
from tkinter import filedialog, messagebox  # A library for opening files and showing messages
from stegano import lsb  # A library for hiding secret messages inside pictures

background = " " #Add the background colour here

# Create the main window for our app
root = ctk.CTk()  # This makes the main window where everything will happen

# This sets the size of the window
root.geometry(" ")
root.resizable(False, False)  # This stops people from resizing the window (it stays the same size)
root.config(bg=background)  # This makes the background color of the window pink
root.title(" ")  # This gives the window a title, which shows at the top of the window

# This keeps the window open and ready to use
root.mainloop()  # This line runs the program and keeps the window open until you close it

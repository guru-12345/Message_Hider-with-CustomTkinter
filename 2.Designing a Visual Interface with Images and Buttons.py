#Task 1- Run the code and identify why the logo is not displaying.
#Task 2- Add the logo_image with a size of (100, 100) using the file logo.png.
#Task 3- Add the decrypt button.


# Importing libraries we need
import customtkinter as ctk   # A library to make cool and modern windows
from PIL import Image, ImageTk    # A library to work with pictures
from tkinter import filedialog, messagebox  # A library for opening files and showing messages
from stegano import lsb  # A library for hiding secret messages inside pictures

background = "grey"
# Create the main window for our app
root = ctk.CTk()  # This makes the main window where everything will happen

root.geometry("600x450")  # This sets the size of the window to be 600 pixels wide and 450 pixels tall
root.resizable(False, False)  # This stops people from resizing the window (it stays the same size)
root.config(bg=background)  # This makes the background color of the window pink
root.title("Message Encoder")  # This gives the window a title, which shows at the top of the window


#logo = ctk.CTkImage(Image.open('#load the image here '), size=(# add the size of the logo))
sender = Image.open('logo.jpg')
sender = sender.resize((240, 240))
label_image = ImageTk.PhotoImage(sender)

open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
encrypt_image = ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
#decrypt_image = ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))
white_image = ctk.CTkImage(Image.open('dark_mode.png'), size=(70, 45))
dark_image = ctk.CTkImage(Image.open('white_mode.png'), size=(70, 45))

#logo_image = ctk.CTkLabel(root, image=logo, text="", fg_color=background)
#logo_image.place(x=0, y=0)

message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.place(x=100, y=20)

PhotoLabel = ctk.CTkLabel(root, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.place(x=10, y=100)

toggle_button = ctk.CTkButton(root, image=dark_image, text="", fg_color=background, hover_color=background)
toggle_button.place(x=480, y=20)

Data_entry = ctk.CTkTextbox(root, width=250, height=200, border_width=5)
Data_entry.place(x=270, y=100)

open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background)
open_button.place(x=100, y=355)

encrypt_button = ctk.CTkButton(root, image=encrypt_image, text="", fg_color=background, hover_color=background)
encrypt_button.place(x=270, y=365)

#add the decrypt button code here

root.mainloop()  # This line runs the program and keeps the window open until you close it

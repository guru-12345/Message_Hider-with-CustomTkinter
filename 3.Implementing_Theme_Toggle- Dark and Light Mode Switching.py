# Write your code here :-)
import customtkinter as ctk   # A library to make cool and modern windows
from PIL import Image, ImageTk    # A library to work with pictures
from tkinter import filedialog, messagebox  # A library for opening files and showing messages
from stegano import lsb  # A library for hiding secret messages inside pictures
# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

background = "#2E2E2E"
file_types = [("PNG files", "*.png")]
file_path = ""

def toggle():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        background = "#FFFFFF"
        toggle_button.configure(fg_color=background, hover = background, image=white_image)
    else:
        ctk.set_appearance_mode("Dark")
        background = "#2E2E2E"
        toggle_button.configure(fg_color=background, hover = background, image=dark_image)

    root.configure(fg_color=background)
    message_label.configure(fg_color=background, text_color="black")
    logo_image.configure(fg_color=background)
    PhotoLabel.configure(fg_color=background)
    Data_entry.configure(fg_color=background)
    open_button.configure(fg_color=background)
    encrypt_button.configure(fg_color=background)
    decrypt_button.configure(fg_color=background)

root = ctk.CTk()  # This makes the main window where everything will happen

root.geometry("600x450")  # This sets the size of the window to be 600 pixels wide and 450 pixels tall
root.resizable(False, False)  # This stops people from resizing the window (it stays the same size)
root.config(bg=background)  # This makes the background color of the window pink
root.title("Message Encoder")  # This gives the window a title, which shows at the top of the window


logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100))
sender = Image.open('logo.jpg')
sender = sender.resize((240, 240))
label_image = ImageTk.PhotoImage(sender)

open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
encrypt_image = ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
decrypt_image = ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))
white_image = ctk.CTkImage(Image.open('dark_mode.png'), size=(70, 45))
dark_image = ctk.CTkImage(Image.open('white_mode.png'), size=(70, 45))

logo_image = ctk.CTkLabel(root, image=logo, text="", fg_color=background)
logo_image.place(x=0, y=0)

message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.place(x=100, y=20)

PhotoLabel = ctk.CTkLabel(root, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.place(x=10, y=100)

toggle_button = ctk.CTkButton(root, image=dark_image, text="", fg_color=background, hover_color=background,command=toggle)
toggle_button.place(x=480, y=20)

Data_entry = ctk.CTkTextbox(root, width=250, height=200, border_width=5)
Data_entry.place(x=270, y=100)

open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background)
open_button.place(x=100, y=355)

encrypt_button = ctk.CTkButton(root, image=encrypt_image, text="", fg_color=background, hover_color=background)
encrypt_button.place(x=270, y=365)

decrypt_button = ctk.CTkButton(root, image=decrypt_image, text="", fg_color=background, hover_color=background)
decrypt_button.place(x=430, y=365)
# This keeps the window open and ready to use
root.mainloop()  # This line runs the program and keeps the window open until you close it

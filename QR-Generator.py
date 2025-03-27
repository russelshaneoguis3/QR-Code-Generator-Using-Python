import os
import qrcode
import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox
from pathlib import Path

# Set up the main window
root = tk.Tk()
root.title("Link QR Code Generator")
root.geometry("400x300")

# Folder to save QR codes
QR_FOLDER = Path(r"C:/Users/russe/OneDrive/Documents/QR-CODES")
QR_FOLDER.mkdir(exist_ok=True)

# Function to open a custom input dialog
def custom_input_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Enter Link")
    dialog.geometry("400x200")
    dialog.grab_set()
    
    label = tk.Label(dialog, text="Enter your link:", font=("Arial", 14))
    label.pack(pady=10)
    
    entry = tk.Entry(dialog, font=("Arial", 14), width=40)
    entry.pack(pady=10)
    
    def submit():
        global link
        link = entry.get()
        dialog.destroy()
    
    button = tk.Button(dialog, text="OK", font=("Arial", 12), command=submit)
    button.pack(pady=10)
    
    dialog.wait_window()

# Function to generate a random string
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate QR code from a link
def generate_qr():
    global link
    link = ""
    custom_input_dialog()
    if link:
        qr = qrcode.make(link)
        file_name = simpledialog.askstring("Input", "Enter file name:")
        if not file_name:
            messagebox.showwarning("Warning", "File name cannot be empty!")
            return
        random_suffix = generate_random_string()
        qr_filename = QR_FOLDER / f"{file_name}_{random_suffix}.jpg"
        qr.save(qr_filename)
        messagebox.showinfo("Success", f"QR Code saved at: {qr_filename}")
        os.startfile(QR_FOLDER)

# UI Elements
label = tk.Label(root, text="Enter a link to generate a QR Code:")
label.pack(pady=10)
button = tk.Button(root, text="Click to Generate", command=generate_qr)
button.pack(pady=20)

# Run the app
root.mainloop()

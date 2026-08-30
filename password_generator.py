import string
import secrets
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Secure Password Generator")
window.geometry("400x300")

title_label = tk.Label(
    window,
    text="Secure Password Generator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

length_label = tk.Label(
    window,
    text="Password length:"
)
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(
    window,
    text="Include digits",
    variable=digits_var
)
digits_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(
    window,
    text="Include lowercase letters",
    variable=lowercase_var
)
lowercase_checkbox.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(
    window,
    text="Include uppercase letters",
    variable=uppercase_var
)
uppercase_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(
    window,
    text="Include symbols",
    variable=symbols_var
)
symbols_checkbox.pack()


def generate_password_gui():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return

    if length < 4 or length > 50:
        messagebox.showerror("Error", "Password length must be between 4 and 50.")
        return

    characters = ""

    if digits_var.get():
        characters += string.digits

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror(
            "Error",
            "Please select at least one character type."
        )
        return

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
    password_var.set(password)


generate_button = tk.Button(
    window,
    text="Generate",
    command=generate_password_gui
)
generate_button.pack()

password_var = tk.StringVar()

result_entry = tk.Entry(
    window,
    textvariable=password_var,
    state="readonly",
    justify="center"
)
result_entry.pack(pady=10)


def copy_password():
    password = password_var.get()
    window.clipboard_clear()
    window.clipboard_append(password)


copy_button = tk.Button(
    window,
    text="Copy",
    command=copy_password
)
copy_button.pack()

window.mainloop()

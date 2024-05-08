################ Program to generate Random password ############

import random
import string
import random
from tkinter import *
from tkinter import ttk

def generate_password():
  """Generates a random password based on user selections."""
  length = int(password_length.get())
  include_upper = uppercase_var.get()
  include_lower = lowercase_var.get()
  include_numbers = numbers_var.get()
  include_symbols = symbols_var.get()

  characters = string.ascii_letters
  if include_upper:
    characters += string.ascii_uppercase
  if include_lower:
    characters += string.ascii_lowercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  password = ''.join(random.choice(characters) for i in range(length))
  password_entry.delete(0, END)
  password_entry.insert(0, password)

# Create the main window
root = Tk()
root.title("Password Generator")
root.geometry("400x300")

# Create labels and entry for password length
password_length_label = ttk.Label(root, text="Password Length:")
password_length_label.pack(pady=10)

password_length = ttk.Spinbox(root, from_=8, to_=32, width=5)
password_length.pack()

# Create checkboxes for character options
uppercase_var = IntVar()
lowercase_var = IntVar()
numbers_var = IntVar()
symbols_var = IntVar()

uppercase_checkbox = ttk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_checkbox = ttk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.pack()

numbers_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

# Create button to generate password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=15)

# Create label and entry to display password
password_label = ttk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = ttk.Entry(root, width=30)
password_entry.pack()

# Copy password to clipboard button (optional)
# You can uncomment this section and add the pyperclip library to enable copy functionality
# from pyperclip import copy
# def copy_password():
#   copy(password_entry.get())
# copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_password)
# copy_button.pack()

root.mainloop()
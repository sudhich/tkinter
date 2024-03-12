import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_name = entry_name.get()
    messagebox.showinfo("Greetings", f"Hello, {user_name}!")

def on_checkbox_click():
    if var_checkbox.get():
        label_checkbox.config(text="Checkbox Checked")
    else:
        label_checkbox.config(text="Checkbox Unchecked")

# Create the main window
app = tk.Tk()
app.title("GUI Application")

# Label Widget
label_name = tk.Label(app, text="Enter Your Name:")
label_name.pack()

# Entry Widget
entry_name = tk.Entry(app)
entry_name.pack()

# Button Widget
button_greet = tk.Button(app, text="Greet", command=on_button_click)
button_greet.pack()

# Checkbox Widget
var_checkbox = tk.BooleanVar()
checkbox = tk.Checkbutton(app, text="Check me", variable=var_checkbox, command=on_checkbox_click)
checkbox.pack()

label_checkbox = tk.Label(app, text="")
label_checkbox.pack()

# Run the main event loop
app.mainloop()

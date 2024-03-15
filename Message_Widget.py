import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Message Widget Example")

# Text to be displayed in the Message widget
message_text = """Welcome to Tkinter!
Tkinter is a Python library for creating graphical user interfaces (GUIs).
With Tkinter, you can create windows, buttons, menus, and more to build interactive applications.
It's a powerful tool for developing desktop applications in Python."""

# Create a Message widget
message = tk.Message(root, text=message_text, width=300, font=("Helvetica", 12))
message.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()

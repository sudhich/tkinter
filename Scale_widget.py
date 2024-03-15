import tkinter as tk

def update_label(value):
    label.config(text="Value: " + str(value))

# Create the main application window
root = tk.Tk()
root.title("Scale Example")

# Create a Scale widget
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_label)
scale.pack(pady=10)

# Create a label to display the value of the Scale
label = tk.Label(root, text="Value: " + str(scale.get()))
label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

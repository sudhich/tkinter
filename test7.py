import tkinter as tk

def update_label():
    label.config(text="Selected option: " + var.get())

# Create the main application window
root = tk.Tk()
root.title("Radiobutton Example")

# Create a StringVar to store the selected option
var = tk.StringVar()

# Set an initial value for the StringVar
var.set("Option 1")

# Create Radiobuttons with different options
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=update_label)
radiobutton1.pack(pady=5)

radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=update_label)
radiobutton2.pack(pady=5)

radiobutton3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=update_label)
radiobutton3.pack(pady=5)

# Create a label to display the selected option
label = tk.Label(root, text="Selected option: " + var.get())
label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

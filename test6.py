import tkinter as tk

def update_label():
    label.config(text="Value1: " + str(var1.get()) + " Value2: " + str(var2.get()) + " Value3: " + str(var3.get()))

# Create the main application window
root = tk.Tk()
root.title("IntVar Example")

# Create IntVars
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Create Checkbuttons with separate IntVars
checkbutton1 = tk.Checkbutton(root, text="Toggle 1", variable=var1, command=update_label)
checkbutton1.pack(pady=10)

checkbutton2 = tk.Checkbutton(root, text="Toggle 2", variable=var2, command=update_label)
checkbutton2.pack(pady=10)

checkbutton3 = tk.Checkbutton(root, text="Toggle 3", variable=var3, command=update_label)
checkbutton3.pack(pady=10)

# Create a label to display the value of the IntVars
label = tk.Label(root, text="Value1: " + str(var1.get()) + " Value2: " + str(var2.get()) + " Value3: " + str(var3.get()))
label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

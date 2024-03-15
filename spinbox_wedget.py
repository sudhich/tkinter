import tkinter as tk

def show_int_value():
    int_value = int_spinbox.get()
    print("Selected integer value:", int_value)

def show_float_value():
    float_value = float_spinbox.get()
    print("Selected float value:", float_value)

# Create the main application window
root = tk.Tk()
root.title("Spinbox Widget Example")

# Integer Spinbox
int_spinbox = tk.Spinbox(root, from_=0, to=10, increment=1, command=show_int_value)
int_spinbox.pack(padx=20, pady=10)

# Float Spinbox
float_spinbox = tk.Spinbox(root, from_=0, to=10, increment=0.1, format="%.1f", command=show_float_value)
float_spinbox.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()

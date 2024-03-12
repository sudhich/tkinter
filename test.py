import tkinter as tk

# Create a window
window = tk.Tk()

# Set the window title
window.title("Place Example")

# Create labels
label1 = tk.Label(window, text="Label 1", bg="lightblue")
label2 = tk.Label(window, text="Label 2", bg="lightgreen")
label3 = tk.Label(window, text="Label 3", bg="lightyellow")
label4 = tk.Label(window, text="Label 4", bg="lightpink")

# Position labels using place
label1.place(x=50, y=30)
label2.place(x=70, y=40)
label3.place(x=50, y=80)
label4.place(x=150, y=80)

# Run the event loop
window.mainloop()

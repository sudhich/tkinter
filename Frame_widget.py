import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Frame Example")

# Create a Frame widget
frame = tk.Frame(root, width=200, height=100, bg="lightblue")
frame.pack(padx=20, pady=20)

# Create some widgets inside the Frame
label = tk.Label(frame, text="This is inside the frame", bg="lightblue")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Click Me", bg="lightblue")
button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

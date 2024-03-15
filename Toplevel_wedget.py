import tkinter as tk

def open_dialog():
    # Create a new Toplevel window
    dialog = tk.Toplevel(root)
    dialog.title("Dialog Box")

    # Add content to the dialog window
    label = tk.Label(dialog, text="This is a dialog box.")
    label.pack(padx=20, pady=10)

    # Add a button to open another Toplevel window
    open_button = tk.Button(dialog, text="Open Another Dialog", command=open_dialog)
    open_button.pack(padx=20, pady=10)

# Create the main application window
root = tk.Tk()
root.title("Main Window")

# Add a button to open the first dialog window
open_button = tk.Button(root, text="Open Dialog", command=open_dialog)
open_button.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()

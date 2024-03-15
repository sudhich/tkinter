import tkinter as tk

def show_selected_option(selected_option):
    print("Selected Option:", selected_option)

# Create the main application window
root = tk.Tk()
root.title("OptionMenu Widget Example")

# Define options for the OptionMenu
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Create a StringVar to store the selected option
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set the default selected option

# Create the OptionMenu widget
option_menu = tk.OptionMenu(root, selected_option, *options, command=show_selected_option)
option_menu.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()

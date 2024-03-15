import tkinter as tk

def file_new():
    print("New file created")

def file_open():
    print("File opened")

def file_save():
    print("File saved")

def file_save_as():
    print("File saved as...")

def file_exit():
    print("Exiting application")
    root.quit()

def edit_cut():
    print("Text cut")

def edit_copy():
    print("Text copied")

def edit_paste():
    print("Text pasted")

def edit_undo():
    print("Undo operation")

def edit_redo():
    print("Redo operation")

# Create the main application window
root = tk.Tk()
root.title("Menu Example")

# Create a Menu widget
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_command(label="Save As...", command=file_save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=file_exit)

# Create "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=edit_undo)
edit_menu.add_command(label="Redo", command=edit_redo)

# Run the Tkinter event loop
root.mainloop()

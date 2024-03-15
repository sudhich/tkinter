import tkinter as tk

def language_selected(language):
    print(f"Language selected: {language}")

# Create the main application window
root = tk.Tk()
root.title("Language Selector")

# Create a function to display the selected language
def language_selected(language):
    print(f"Language selected: {language}")

# Create a Menubutton widget
menu_button = tk.Menubutton(root, text="Select Language", relief=tk.RAISED)
menu_button.pack()

# Create a Menu widget for the Menubutton
menu = tk.Menu(menu_button, tearoff=False)
menu_button.configure(menu=menu)

# Add language options to the Menu
languages = ["Hindi", "English", "Telugu", "Exit"]
for language in languages:
    if language == "Exit":
        menu.add_separator()
        menu.add_command(label=language, command=root.quit)
    else:
        menu.add_command(label=language, command=lambda lang=language: language_selected(lang))

# Run the Tkinter event loop
root.mainloop()

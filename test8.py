import tkinter as tk

def get_selection():
    # Get the index of the selected item
    index = listbox.curselection()
    if index:
        # Retrieve the selected item using the index
        selected_item = listbox.get(index)
        # Update the label to display the selected item
        label.config(text="Selected item: " + selected_item)
    else:
        label.config(text="No item selected")

def delete_selection():
    # Get the index of the selected item
    index = listbox.curselection()
    if index:
        # Delete the selected item from the Listbox
        listbox.delete(index)
        label.config(text="Item deleted")
    else:
        label.config(text="No item selected")

# Create the main application window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack()

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Create a button to get the selected item
button_get = tk.Button(root, text="Get Selection", command=get_selection)
button_get.pack(pady=5)

# Create a button to delete the selected item
button_delete = tk.Button(root, text="Delete Selection", command=delete_selection)
button_delete.pack(pady=5)

# Create a label to display the selected item or deletion message
label = tk.Label(root, text="Selected item: ")
label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

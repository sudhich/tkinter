import tkinter as tk

def scroll_text(*args):
    text.yview(*args)

# Create the main application window
root = tk.Tk()
root.title("Scrollbar Example")

# Create a Text widget
text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text.pack(side=tk.LEFT, fill=tk.Y)

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(root, command=scroll_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget to use the Scrollbar
text.config(yscrollcommand=scrollbar.set)

# Add some sample text to the Text widget
for i in range(20):
    text.insert(tk.END, f"Line {i}\n")

# Run the Tkinter event loop
root.mainloop()

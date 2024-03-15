import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("PanedWindow Widget Example")

# Create a PanedWindow widget
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Add frames to the PanedWindow
frame1 = tk.Frame(paned_window, background="lightblue", width=100, height=300)
frame2 = tk.Frame(paned_window, background="lightgreen", width=100, height=300)

paned_window.add(frame1)
paned_window.add(frame2)

# Run the Tkinter event loop
root.mainloop()

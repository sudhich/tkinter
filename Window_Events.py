'''
#1st program
import tkinter as tk

def on_closing():
    print("Window is closing")
    root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind to window close event
root.mainloop()
'''

'''
#2nd program
import tkinter as tk

def on_resize(event):
    print("Window resized to", event.width, "x", event.height)

root = tk.Tk()

# Bind to window resize event
root.bind("<Configure>", on_resize)

root.mainloop()
'''


import tkinter as tk

def on_move(event):
    print("Window moved to", event.x, ",", event.y)

root = tk.Tk()

# Bind to window move event
root.bind("<Configure>", on_move)

root.mainloop()

'''
#1st program
import tkinter as tk

def mouse_clicked(event):
    print("Mouse clicked at", event.x, event.y)

root = tk.Tk()
root.bind("<Button-1>", mouse_clicked)  # Bind to left mouse button click
root.mainloop()
'''

'''
#2nd program
import tkinter as tk

def mouse_released(event):
    print("Mouse released at", event.x, event.y)

root = tk.Tk()
root.bind("<ButtonRelease-1>", mouse_released)  # Bind to left mouse button release
root.mainloop()
'''

'''
#3rd program
import tkinter as tk

def mouse_moved(event):
    print("Mouse moved to", event.x, event.y)

root = tk.Tk()
root.bind("<Motion>", mouse_moved)  # Bind to mouse movement
root.mainloop()
'''


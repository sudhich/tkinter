'''#1st program
import tkinter as tk

def key_pressed(event):
    print("Key pressed:", event.keysym)

root = tk.Tk()
root.bind("<Key>", key_pressed)  # Bind to any key press
root.mainloop()
'''


'''
#2nd program
import tkinter as tk

def key_a_pressed(event):
    print("Key 'a' pressed")

root = tk.Tk()
root.bind("<KeyPress-a>", key_a_pressed)  # Bind to 'a' key press
root.mainloop()
'''

'''
#3rd program
import tkinter as tk

def key_combination_pressed(event):
    if event.keysym == "a" and event.state == 4:  # Check if 'a' key and Control modifier are pressed
        print("Ctrl+A pressed")

root = tk.Tk()
root.bind("<Control-a>", key_combination_pressed)  # Bind to Ctrl+A key combination
root.mainloop()
'''

import tkinter as tk

def key_released(event):
    print("Key released:", event.keysym)

root = tk.Tk()
root.bind("<KeyRelease>", key_released)  # Bind to any key release
root.mainloop()

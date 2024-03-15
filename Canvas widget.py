import tkinter as tk

def draw_circle(event):
    x = event.x
    y = event.y
    radius = 20
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")

def draw_rectangle(event):
    x = event.x
    y = event.y
    width = 40
    height = 20
    canvas.create_rectangle(x - width/2, y - height/2, x + width/2, y + height/2, fill="red")

def draw_line(event):
    x = event.x
    y = event.y
    canvas.create_line(x, y, x + 50, y + 50, fill="green")

def draw_polygon(event):
    x = event.x
    y = event.y
    canvas.create_polygon(x, y, x+20, y+40, x-20, y+40, fill="yellow")

def draw_text(event):
    x = event.x
    y = event.y
    canvas.create_text(x, y, text="Hello!", fill="purple")

# Create the main application window
root = tk.Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Bind different mouse events to corresponding drawing functions
canvas.bind("<Button-1>", draw_circle)
canvas.bind("<Button-2>", draw_line)
canvas.bind("<Button-3>", draw_rectangle)
canvas.bind("<Shift-Button-1>", draw_polygon)
canvas.bind("<Control-Button-1>", draw_text)

# Run the Tkinter event loop
root.mainloop()

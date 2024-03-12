import tkinter as tk

root=tk.Tk()
root.title("place Geo")
parent=tk.Frame(root, width=400, height=400, bg="blue")
parent.pack()
child=tk.Label(parent, text="Hello world!", bg="white", fg="black", font=("Helvetica", 16))
child.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.5, anchor="se", bordmode="inside", x=65, y=70,)

root.mainloop()

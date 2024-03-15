import tkinter as tk
from tkinter import messagebox

def submit_info():
    name = name_entry.get()
    age = age_entry.get()
    id_number = id_entry.get()
    password = password_entry.get()
    
    # Perform validation
    if not name or not age or not id_number or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    # Perform additional validation if needed
    
    # Display collected information
    messagebox.showinfo("Submitted Information",
                        f"Name: {name}\nAge: {age}\nID: {id_number}\nPassword: {password}")

# Create the main application window
root = tk.Tk()
root.title("Personal Information")

# Create a LabelFrame widget
info_frame = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
info_frame.pack(padx=20, pady=20)

# Create Labels and Entry widgets for each piece of information
name_label = tk.Label(info_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="e")

name_entry = tk.Entry(info_frame)
name_entry.grid(row=0, column=1, pady=5)

age_label = tk.Label(info_frame, text="Age:")
age_label.grid(row=1, column=0, sticky="e")

age_entry = tk.Entry(info_frame)
age_entry.grid(row=1, column=1, pady=5)

id_label = tk.Label(info_frame, text="ID:")
id_label.grid(row=2, column=0, sticky="e")

id_entry = tk.Entry(info_frame)
id_entry.grid(row=2, column=1, pady=5)

password_label = tk.Label(info_frame, text="Password:")
password_label.grid(row=3, column=0, sticky="e")

password_entry = tk.Entry(info_frame, show="*")
password_entry.grid(row=3, column=1, pady=5)

# Create a button to submit the information
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

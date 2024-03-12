import tkinter as tk

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Create and place GUI elements
label_num1 = tk.Label(app, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(app, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

btn_calculate = tk.Button(app, text="Calculate Sum", command=calculate_sum)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(app, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main event loop
app.mainloop()

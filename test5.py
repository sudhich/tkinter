import tkinter as tk
from tkinter import messagebox

class ExpressionCalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Expression Calculator")

        self.expression = ""

        self.entry = tk.Entry(master, font=('Helvetica', 14), width=20, justify="right")
        self.entry.grid(row=0, column=0, columnspan=3)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('DEL', 4, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, font=('Helvetica', 14), width=5, height=2,
                               command=lambda txt=text: self.button_click(txt))
            button.grid(row=row, column=col)

    def button_click(self, value):
        if value == '=':
            try:
                self.expression = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
        elif value == 'DEL':
            self.expression = self.expression[:-1]
            self.entry.delete(len(self.expression), tk.END)
        else:
            self.expression += value
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    app = ExpressionCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

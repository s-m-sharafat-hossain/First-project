import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.expression = ""
        self.text_input = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.text_input, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (text, row, col, *span) in buttons:
            colspan = span[0] if span else 1
            tk.Button(master, text=text, padx=20, pady=20, font=('Arial', 18),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except Exception:
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
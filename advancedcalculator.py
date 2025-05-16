import tkinter as tk
import math

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("400x500")
        self.configure(bg="#1f1f2e")

        self.expression = ""

        self.display_frame = tk.Frame(self, bg="#2c2c3e")
        self.display_frame.pack(expand=True, fill="both")

        self.display = tk.Entry(self.display_frame, font=("Arial", 20), bg="#3b3b4f", fg="#ffffff", bd=0, justify="right")
        self.display.pack(expand=True, fill="both")

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', '√',
            'log', 'π', 'e', '^', 'C'
        ]

        row = 0
        col = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, font=("Arial", 14), fg="#ffffff", bg="#4a4a5c",
                      activebackground="#6b6b82", command=action).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
        elif value == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif value in ("sin", "cos", "tan", "√", "log", "π", "e"):
            self.expression = self.handle_advanced(value)
        else:
            self.expression += value

        self.update_display()

    def handle_advanced(self, function):
        try:
            if function == "sin":
                return str(math.sin(math.radians(float(self.expression))))
            elif function == "cos":
                return str(math.cos(math.radians(float(self.expression))))
            elif function == "tan":
                return str(math.tan(math.radians(float(self.expression))))
            elif function == "√":
                return str(math.sqrt(float(self.expression)))
            elif function == "log":
                return str(math.log10(float(self.expression)))
            elif function == "π":
                return str(math.pi)
            elif function == "e":
                return str(math.e)
        except Exception:
            return "Error"

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.mainloop()

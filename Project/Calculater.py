import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self):
        self.result = 0
        self.current = ""
        self.operation = None

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulo(self, a, b):
        if b == 0:
            return "Error"
        return a % b

    def calculate(self, operand1, operation, operand2):
        try:
            a = float(operand1)
            b = float(operand2)
            
            if operation == "+":
                return self.add(a, b)
            elif operation == "-":
                return self.subtract(a, b)
            elif operation == "*":
                return self.multiply(a, b)
            elif operation == "/":
                return self.divide(a, b)
            elif operation == "^":
                return self.power(a, b)
            elif operation == "%":
                return self.modulo(a, b)
        except:
            return "Error"


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg="#2c3e50")

        self.calculator = Calculator()
        self.display_value = ""
        self.stored_value = ""
        self.operation = None

        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, bg="#34495e", height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        display_frame.pack_propagate(False)

        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 36, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            justify=tk.RIGHT,
            anchor="e"
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        button_layout = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "^", "="]
        ]

        button_font = font.Font(family="Arial", size=14, weight="bold")

        for row in button_layout:
            row_frame = tk.Frame(buttons_frame, bg="#2c3e50")
            row_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

            for btn_text in row:
                self.create_button(row_frame, btn_text, button_font)

    def create_button(self, parent, text, font):
        if text == "=":
            bg_color = "#27ae60"
            fg_color = "#fff"
        elif text in ["C", "←"]:
            bg_color = "#e74c3c"
            fg_color = "#fff"
        elif text in ["/", "*", "-", "+", "%", "^"]:
            bg_color = "#f39c12"
            fg_color = "#fff"
        else:
            bg_color = "#34495e"
            fg_color = "#ecf0f1"

        btn = tk.Button(
            parent,
            text=text,
            font=font,
            bg=bg_color,
            fg=fg_color,
            command=lambda: self.on_button_click(text),
            relief=tk.RAISED,
            bd=2,
            activebackground=bg_color,
            activeforeground=fg_color
        )
        btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=2, pady=2)

    def on_button_click(self, char):
        if char == "C":
            self.display_value = ""
            self.stored_value = ""
            self.operation = None
            self.update_display()

        elif char == "←":
            self.display_value = self.display_value[:-1]
            self.update_display()

        elif char in ["+", "-", "*", "/", "%", "^"]:
            if self.display_value and self.display_value != "Error":
                self.stored_value = self.display_value
                self.operation = char
                self.display_value = ""
                self.update_display()

        elif char == "=":
            if self.stored_value and self.operation and self.display_value:
                result = self.calculator.calculate(
                    self.stored_value,
                    self.operation,
                    self.display_value
                )
                self.display_value = str(result)
                self.stored_value = ""
                self.operation = None
                self.update_display()

        elif char == ".":
            if "." not in self.display_value:
                self.display_value += char
                self.update_display()

        else:
            self.display_value += char
            self.update_display()

    def update_display(self):
        if self.display_value == "":
            text = "0"
        else:
            text = self.display_value

        if len(text) > 15:
            text = text[:15]

        self.display.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()

import tkinter as tk

class FourtProject:
    def __init__(self, master):
        self.master = master
        self.master.title("Fourt Project")

        self.label = tk.Label(master, text="Welcome to Fourt Project!")
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FourtProject(root)
    root.mainloop() 

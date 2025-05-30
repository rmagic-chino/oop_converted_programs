import tkinter as tk

class BaseGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Maker")
        self.root.geometry("420x520")
        
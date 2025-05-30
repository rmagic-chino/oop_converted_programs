import tkinter as tk
from question_loader import QuestionLoader
from quiz_logic import QuizLogic

class QuizGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Application")
        self.root.geometry("450x400")
        self.root.resizable(False, False)
        self.root.config(bg="#111")
        
        self.loader = QuestionLoader()
        self.logic = None
        
        self.setup_widgets()
        
    
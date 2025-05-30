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
        
    def setup_widgets(self):
        tk.Button(
            self.root, 
            text="Load Questions",
            command=self.load_questions,
            font=("Arial", 14),
        ).pack(pady=10)
        
        self.question_label = tk.Label(
            self.root, 
            text="Press 'Load Questions' to start",
            font=("Arial", 16),
            bg="#111",
            fg="white"
        )
        self.question_label.pack(pady=20)
        
        self.answer_buttons = []
        for option in ['a', 'b', 'c', 'd']:
            button = tk.Button(
                self.root,
                text=option.upper(),
                width=30,
                command=lambda opt=option: self.logic.check_answer(opt)
            )
            button.pack(pady=5)
            self.answer_buttons.append(button)
            
    def load_questions(self):
        questions = self.loader.load_from_file()
        if questions:
            self.logic = QuizLogic(
                questions, 
                on_question_change=self.update_question,
                on_quiz_end=self.root.destroy
            )
            self.logic.next_question()
     
    def update_question(self, question_data):
        self.question_label.config(text=question_data['q'])
        options = ['a', 'b', 'c', 'd']
        for i, option in enumerate(options):
            self.answer_buttons[i].config(text=question_data[option])
            
    def run(self):
        self.root.mainloop()
        
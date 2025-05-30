import random
from tkinter import messagebox

class QuizLogic:
    def __init__(self, questions, on_question_change, on_quiz_end):
        self.questions = questions
        self.current_question = {}
        self.on_question_change = on_question_change
        self.on_quiz_end = on_quiz_end
        
    def next_question(self):
        if not self.questions:
            messagebox.showinfo("Quiz Ended", "No more questions available.")
            self.on_quiz_end()
            return
        
        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)
        self.on_question_change(self.current_question)
        
    def check_answer(self, selected_option):
        correct = self.current_question['correct']
        if selected_option == correct:
            messagebox.showinfo("Correct!", "Tama boss!")
        else:
            messagebox.showerror("Incorrect", f"Mali boss! Ang tamang sagot ay {correct}.")
        self.next_question()
        
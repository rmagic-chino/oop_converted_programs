import random
from tkinter import messagebox

class QuizLogic:
    def __init__(self, questions, on_question_change, on_quiz_end):
        self.questions = questions
        self.current_question = {}
        self.on_question_change = on_question_change
        self.on_quiz_end = on_quiz_end
        
    
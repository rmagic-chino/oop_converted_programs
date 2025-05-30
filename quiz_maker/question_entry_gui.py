import tkinter as tk
from tkinter import messagebox
from base_gui import BaseGUI

class QuestionEntryGUI(BaseGUI):
    def __init__(self, question_bank, file_manager):
        super().__init__()
        self.question_bank = question_bank
        self.file_manager = file_manager
        
        self.question_text = tk.Entry(self.root, width=60)
        self.option_a_entry = tk.Entry(self.root, width=60)
        self.option_b_entry = tk.Entry(self.root, width=60)
        self.option_c_entry = tk.Entry(self.root, width=60)
        self.option_d_entry = tk.Entry(self.root, width=60)
        self.correct_option = tk.StringVar()
        

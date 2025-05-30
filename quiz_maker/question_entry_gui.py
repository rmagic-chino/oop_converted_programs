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
        
        self._build_form()
        
    def _build_form(self):
        tk.Label(self.root, text="Enter your question:").pack()
        self.question_text.pack()
        
        tk.Label(self.root, text="Option A:").pack()
        self.option_a_entry.pack()
        
        tk.Label(self.root, text="Option B:").pack()
        self.option_b_entry.pack()
        
        tk.Label(self.root, text="Option C:").pack()
        self.option_c_entry.pack()
        
        tk.Label(self.root, text="Option D:").pack()
        self.option_d_entry.pack()
        
        tk.Label(self.root, text="Correct Option:").pack()
        radio_frame = tk.Frame(self.root)
        radio_frame.pack()
        
        for option in ['a', 'b', 'c', 'd']:
            tk.Radiobutton(
                radio_frame,
                text=option,
                variable=self.correct_option,
                value=option
            ).pack(anchor='w')
            
        tk.Button(
            self.root,
            text="Add Question",
            width=20,
            command=self.submit_question  
        ).pack(pady=10)
        
        tk.Button(
            self.root,
            text="Exit",
            width=20,
            command=self._on_exit
        ).pack()
        
    def submit_question(self):
        is_added = self.question_bank.add_question(
            self.question_text.get(),
            self.option_a_entry.get(),
            self.option_b_entry.get(),
            self.option_c_entry.get(),
            self.option_d_entry.get(),
            self.correct_option.get()
        )
        
        if is_added:
            messagebox.showinfo("Success", "Question added successfully!")
            self._clear_fields()
        else:
            messagebox.showerror("Error", "Failed to add question. Please check your inputs.")
            
    def _clear_fields(self):
        self.question_text.delete(0, tk.END)
        self.option_a_entry.delete(0, tk.END)
        self.option_b_entry.delete(0, tk.END)
        self.option_c_entry.delete(0, tk.END)
        self.option_d_entry.delete(0, tk.END)
        self.correct_option.set(None)
        
    def _on_exit(self):
        should_save = messagebox.askyesno(
            "Exit",
            "Do you want to save the questions before exiting?"
        )
        if should_save:
            self.file_manager.save_to_file()
        self.root.destroy()
        
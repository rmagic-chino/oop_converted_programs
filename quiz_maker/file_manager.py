from tkinter import messagebox, filedialog

class FileManager:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        
    def save_to_file(self):
        if self.question_bank.is_empty():
            messagebox.showwarning("Warning", "No questions to save.")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Question As"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    for question in self.question_bank.get_all_questions():
                        file.write(f"{question['question']}\n")
                        file.write(f"A: {question['a']}\n")
                        file.write(f"B: {question['b']}\n")
                        file.write(f"C: {question['c']}\n")
                        file.write(f"D: {question['d']}\n")
                        file.write(f"Correct: {question['correct']}\n\n")
                        
                messagebox.showinfo("Saved", f"Questions saved to: \n{file_path}")
            except Exception as error:
                messagebox.showerror("Error", f"Failed to save questions: {error}")
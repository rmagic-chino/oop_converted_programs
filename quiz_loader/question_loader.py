from tkinter import filedialog, messagebox

class QuestionLoader:
    def __init__(self):
        self.questions = []
        
    def load_from_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return []
        
        with open(path, 'r') as file:
            blocks = file.read().strip().split('\n\n')
            
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) == 6:
                self.questions.append({
                    'q': lines[0][9:],
                    'a': lines[1][3:],
                    'b': lines[2][3:],
                    'c': lines[3][3:],
                    'd': lines[4][3:],
                    'correct': lines[5][9:]
                })
                
        if not self.questions:
            messagebox.showerror("Error", "No valid questions found in the file.")
        return self.questions
    
            
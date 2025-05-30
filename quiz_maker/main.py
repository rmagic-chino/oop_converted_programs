from question_bank import QuestionBank
from file_manager import FileManager
from question_entry_gui import QuestionEntryGUI

if __name__ == "__main__":
    bank = QuestionBank()
    mananger = FileManager(bank)
    app = QuestionEntryGUI(bank, mananger)
    app.root.mainloop()
    
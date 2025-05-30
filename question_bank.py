class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(
            self,
            question_text,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_option,
    ):
        if (
            not question_text or
            not option_a or
            not option_b or
            not option_c or
            not option_d or
            correct_option not in ['a', 'b', 'c', 'd']
        ):
            return False
        
        question_data = {
            'question': question_text,
            'a': option_a,
            'b': option_b,
            'c': option_c,
            'd': option_d,
            'correct': correct_option
        }
        self.questions.append(question_data)
        return True
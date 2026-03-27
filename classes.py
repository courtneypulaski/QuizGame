class Quiz:
    def __init__(self,name,questions,answers,correct):
        self.name = name
        self.questions = questions
        self.answers = answers
        self.correct = correct

    @property
    def name(self):
        return self._name
    
    @property
    def questions(self):
        return self._questions
    
    @property
    def answers(self):
        return self._answers
    
    @property
    def correct(self):
        return self._correct
    
    @name.setter
    def name(self, name):
        self._name = name

    @questions.setter
    def questions(self, questions):
        self._questions = questions

    @answers.setter
    def answers(self, answers):
        self._answers = answers

    @correct.setter
    def correct(self, correct):
        self._correct = correct
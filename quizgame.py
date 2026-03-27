import random

questions = ["Type the letters ABC?",
             "Type the letters XYZ?",
             "Type the letters MNO?"]

answers = [("ABC","DEF","GHI"),
           ("LMN","ABC","XYZ","OPQ"),
           ("HIJ","UVW","MNO","JKL")]

correct = [0,2,2]

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


shapesQuiz = Quiz("Shapes",
                  ["Type the letters ABC?",
                   "Type the letters XYZ?",
                   "Type the letters MNO?"],
                   [("ABC","DEF","GHI"),
                    ("LMN","ABC","XYZ","OPQ"),
                    ("HIJ","UVW","MNO","JKL")],
                    [0,2,2]
                   )

quiz1 = Quiz("Quiz1",["1","2"],["1","2"],[1])
quiz2 = Quiz("Quiz2",["1","2"],["1","2"],[1])

quizzes = [quiz1, quiz2, shapesQuiz]

def main():
    print("Pick a quiz from the following list:")
    for i, item in enumerate(quizzes):
        print(f"{i+1}: {item.name}")
    while True:
        quizSelection = input("Select a quiz, or Quit: ")
        if quizSelection.lower() == "quit":
            print("Goodbye")
            break
        quizSelection = int(quizSelection)
        if quizSelection <= len(quizzes):
            if quiztime(quizzes[quizSelection-1]):
                break
            else:
                for i, item in enumerate(quizzes):
                    print(f"{i+1}: {item.name}")
        else:
            print("Try again!")

def quiztime(quizName):
    order_list = [i for i in range(len(quizName.questions))]
    random.shuffle(order_list)
    #print(order_list)
    for o in order_list:
        print(quizName.questions[o])
        answer_list = [j for j in range(len(quizName.answers[o]))]
        random.shuffle(answer_list)
        for q, item in enumerate(answer_list):
            print(f"{q+1}: {quizName.answers[o][item]}")
        userAnswer = input("Answer? ")
        if userAnswer.lower() == "quit":
            return True
        userAnswer=int(userAnswer)
        if userAnswer > len(quizName.answers[o]):
            print("Invalid Guess")
        elif quizName.answers[o][answer_list[userAnswer-1]] == quizName.answers[o][quizName.correct[o]]:
            print("Correct!")
        else:
            print(f"Incorrect, the correct answer is {quizName.answers[o][quizName.correct[o]]}")

if __name__=="__main__":
    main()
import random
from classes import Quiz
from setup import generateQuizList

quizzes = generateQuizList()

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
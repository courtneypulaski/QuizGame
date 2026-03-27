from classes import Quiz

def generateQuizList():

    #Quiz 1 - Shapes
    name = "Shapes"

    questions = ["Type the letters ABC?",
                "Type the letters XYZ?",
                "Type the letters MNO?"]
    
    answers = [("ABC","DEF","GHI"),
               ("LMN","ABC","XYZ","OPQ"),
               ("HIJ","UVW","MNO","JKL")]
    
    correct = [0,2,2]
    
    shapesQuiz = Quiz(name,questions,answers,correct)

    #Quiz 2 - Test
    name = "Quiz1"
    questions = ["1","2"]
    answers = ["1","2"]
    correct = [1]

    quiz1 = Quiz(name,questions,answers,correct)

    name = "Quiz2"
    quiz2 = Quiz(name,questions,answers,correct)

    return [shapesQuiz, quiz1, quiz2]
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#I created a empty list to store the questions came from the question data
question_bank =[]
#the question will loop through the question data and the question_text gets the question and similarly the answer to
#the question_answer.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    #I created a variable new_question and passed two parameters to the Question class.
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
#constructed an object for the QuizBrian class which is quiz. And we are passing a parameter to the QuizBrain class.
quiz = QuizBrain(question_bank)
#if the still_has_function is true it will go to the next question and if it false it will come out of the program.
while quiz.still_has_question():
    quiz.next_question()

    if not quiz.still_has_question():
        print("YOU HAVE COMPLETED THE QUIZ.")
        print(f"AND YOUR FINAL SCORE IS {quiz.score}/{quiz.question_number}")


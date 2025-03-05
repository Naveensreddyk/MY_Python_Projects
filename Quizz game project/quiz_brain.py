class QuizBrain:

    def __init__(self, question_list):
        #we are assigned this question_number to 0 because question starts from 0. So, we make it a default value.
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        # it will directly return true or false based on the statement.
        return self.question_number < len(self.question_list)

    def next_question(self):
        """from the whole bunch of questions from the question list we are taking the 1st question which index value is
        0. Now, the current_question variable gets the hold of 1st question form the list of questions"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        """Instead, we should access the text attribute of the Question object to display the actual question text"""
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (TRUE/FALSE):\n")
        self.check_answer(user_answer, current_question.answer)

#I created a new method to check if the user entered the correct answer. So, I passed to parameters user_answer and
#correct_answer.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right!")
            print(f"Your Score is {self.score}/{self.question_number}")
            print("\n")
        else:
            print("You are wrong")
            print(f"Your Score is {self.score}/{self.question_number}")
            print("\n")








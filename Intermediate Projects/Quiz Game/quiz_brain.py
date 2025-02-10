class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self,):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        return self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
            print(f"your current score is {self.score}/{self.question_number}")
            print(f"the correct answer is {correct_answer}")
            return True
        else:
            print("you got it wrong")
            print(f"the correct answer is {correct_answer}")
            print("Game over!")
            return False
       



 
         
from sys import set_coroutine_origin_tracking_depth


class QuizBrain:

    """
    A representation a QuizBrain
    """

    def __init__(self, question_list):
        """Constructs all the necessary attributes for the QuizBrain object. 

        Parameters
        ----------
        question_list: Array to Question

        """

        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """TODO: Docstring for next_question.

        Returns
        -------
        TODO

        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        if self.check_answer(user_answer, current_question.answer):
            self.score =+ 1
         
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")

        print(f"The correct answer was {question_answer}")
        print(f"You current score is:  {self.score}")


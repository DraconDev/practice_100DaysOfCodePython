class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        # test = (self.questions_list[self.question_number])

        print(self.question_number)
        print(
            f'Q.{self.question_number+1}:{self.questions_list[self.question_number].text}. True or False?')
        answer = input().lower()
        # test = self.questions_list[self.question_number].answer.lower()
        if answer == self.questions_list[self.question_number].answer.lower():
            # print(self.score)
            self.score += 1
        self.question_number += 1

    def still_has_questions(self):
        # print(len(self.questions_list))
        return len(self.questions_list) > self.question_number

    def get_score(self):
        print(f"Your score: {self.score}/{len(self.questions_list)}")

    def final_score(self):
        print(f"Your final score: {self.score}/{len(self.questions_list)}")

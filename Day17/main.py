from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

questions = []
for item in question_data:
    questions.append(Question(item['text'], item['answer']))

quiz_brain = Quizbrain(questions)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    quiz_brain.get_score()

quiz_brain.final_score()

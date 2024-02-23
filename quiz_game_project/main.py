from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for it in range(len(question_data)):
#     new_q = Question(question_data[it]["text"], question_data[it]["answer"])
#     question_bank.append(new_q)

for q in question_data:
    new_q = Question(q["question"], q["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

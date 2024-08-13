from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(q_text= question_text, q_answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{len(question_data)}")
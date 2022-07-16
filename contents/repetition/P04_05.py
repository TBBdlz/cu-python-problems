"""
	P04-05: checking multiple choice
"""


answers: str = input()
student_answer: str = input()

if len(student_answer) != len(answers):
    print('Incomplete answer')
else:
    score: int = sum(student_answer[i] == answers[i]
                     for i in range(len(student_answer)))
    print(score)

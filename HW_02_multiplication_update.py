import random

correct_answers = 0
question_summary = []

for i in range(1, 11):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    user_answer = int(input(f"Q{i}: {num1} x {num2} = "))
    if user_answer == answer:
        question_summary.append(f"Q{i}: {num1} x {num2} = {user_answer} (Correct)")
        correct_answers += 1
    else:
        question_summary.append(f"Q{i}: {num1} x {num2} = {user_answer} (Incorrect)")

print("\n10 Question Summary:\n")
for question in question_summary:
    print(question)

print(f"\nYou answered {correct_answers} out of 10 questions correctly.")
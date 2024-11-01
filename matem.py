import random

def generate_math_question(a: int, b: int) -> str:
    num = random.randint(a, b)
    ber = random.choice(('*', '+', '-', '/'))
    num2 = random.randint(a, b)
    return f'{num} {ber} {num2}'

# print(generate_math_question(1, 8))

def check_answer(quest: str, answer: str) -> bool:
    try:
        answer = float(answer)
        right_answer = eval(quest)
        return answer == right_answer
    except ValueError:
        return False

# print(check_answer("2 + 3", "5"))
# print(check_answer("5 * 3", "10"))
# print(check_answer("10-3", "семь"))



def math_quiz(number_of_questions: int = 5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        math_ques = generate_math_question()
        user_answer = input(f'{math_ques} = ')
        if check_answer(math_ques, user_answer):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers > number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers > number_of_questions * 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz(7)

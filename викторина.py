# print('Добро пожаловать в квиз по стартапам!')
# print('Ответь на следующие вопросы: ')
#
# question = 'Как называется компания, которая создается для развития новой идеи или инновационного продукта?'
#
# answer = 'Стартап'
#
# print(question)
#
# user_input = input('Введи свой ответ: ')
# print()
# print(user_input)
# if user_input.lower() == answer.lower():
#     print('Правильно!:)')
# else:
#     print('Неправильно.')


import os
import random

clear = lambda: os.system('cls')

print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобу продолжить*')
clear()
print('Поехали!')

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    for sumb in word:
        if sumb in letters:
            print(sumb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты угадал! Молодец!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток: {hp}')

if hp == 0:
    print('Ты проиграл! У тебя закончилось количество попыток.')

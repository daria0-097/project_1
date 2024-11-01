# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters.index('p'))
# print(letters.index('y'))
# print(letters.index('t'))
# print(letters.index('h'))
# print(letters.index('o'))
# print(letters.index('n'))


# line_1 = "Python"
# line_2 = "Java"
# line_3 = "Go"
# print(int((len(line_1) + len(line_2) + len(line_3))/3))


# namber1 = int(input())
# namber2 = int(input())
# if namber1 < namber2:
#     print(namber1)
# else:
#     print(namber2)


# message = "Делать зарядку нужно каждую неделю!"
# x = message.replace('каждую неделю', 'каждый день')
# print(x)


# a = 'Привет, я изучаю Python!'
# print(a[-7])


# weather = 'солнце'
# if weather == 'солнце':
#     print('на улице тепло')
# else:
#     print('на улице холодно')


# money = int(input())
# if money >= 35:
#     print('Оплата прошла успешно')
#     money = money - 35
# else:
#     print('Недостаточно средств')
#
# print("Осталось: ", money)


# ticket = input()
#
# if ticket == 'Сочи':
#     print('Проходите на поезд')
# if ticket == 'НЕ Сочи':
#     print('Ваш поезд ушёл 2 часа назад')


# money = int(input())
# if money >= 35:
#     print('Оплата прошла успешно')
#     money = money - 35
# else:
#     print('Недостаточно средств')


# print("Осталось: ", money)
# username = input()
# if username == 'superuser':
#     print('Вам доступны права суперпользователя')
# else:
#     print('Вам доступны права обычного пользователя')



# is_open = False
#
# days = int(input())
#
# if not is_open:
# print("Магазин открыт!")
# days = days + 1
#
# print("Количество дней: ", days)


# story = "Ехал грека через реку, видит грека - в реке рак. Сунул грека руку в реку, рак за руку греку - цап!"
# old = input("Введите слово, которое нужно заменить: ")
# new = input("Введите слово-заменитель: ")
# story = story.replace(old, new)
# print(story)


# print("Меню:")
# print("1. Шаверма")
# print("2. Шаурма")
# print("3. Фалафель")
# print("4. Самса")
#
# food_number = input("Введите номер блюда, которое хотите заказать: ")
#
# if food_number == "1":
#     print("Вы заказали шаверму!")
# elif food_number == '2':
#     print('Вы заказзали шаурму!')
# elif food_number == '3':
#     print('Вы заказзали фалафель!')
# elif food_number == '2':
#     print('Вы заказзали самсу!')
# else:
#     print('Блюда с таким номером нет.')

# order_cost = 250 # стоимость заказа
# discount_cost = 1 # множитель скидки. Если 1, то платят полную стоимость, если 0, то не платят ничего.
#
# age = int(input("Введите свой возраст: "))
#
# if age < 18:
#     print('Стоимость заказа со скидкой:', order_cost * 0.95)
#
# elif age < 30:
#     print('Стоимость заказа со скидкой:', order_cost * 0.85)
#
# elif age < 60:
#     print('Стоимость заказа со скидкой:', order_cost * 0.75)
#
# elif age < 100:
#     print(order_cost * 0.5)
#
# print("Стоимость заказа со скидкой:", order_cost * discount_cost)


# num = int(input())
# for i in range (0, num):
#     print('квадрат числа i равен i**2')


# day = 1
#
# while day <= 30:
#     print(f'Я перевернул календарь, а там {day} сентября')
#     day += 1
# print("Сентябрь закончился")


# count = 4
#
# while count <= 100:
#     print(count)
#     count += 3


# number = 3
#
# print("Попробуй угадать число от 0 до 5!")
#
# user_number = int(input("Введи число: "))
#
# while number == user_number:
#     print(f'Это верно, я загадал число {number}')
#     break
# else:
#     print('Не угадал')

# import random
#
# number = random.randint(0, 5)
#
# print("Попробуй угадать число от 0 до 5!")
#
# user_number = int(input("Введи число: "))
# while number == user_number:
#     print(f'Это верно, я загадал число {number}')
#     break
# else:
#     print('Не угадал')

# import random
#
# number = random.randint(0, 5)
#
# print("Попробуй угадать число от 0 до 5!")
#
# user_number = int(input("Введи число: "))
#
# attempts = 1
#
# while user_number != number and attempts <3:
#     print('Не угадал')
#     user_number = int(input("Введи число: "))
#     attempts += 1
#
# if user_number == number:
#     print("Это верно, я загадал число", number)
#     print('Ты выиграл')
# else:
#     print('Ты проиграл')

# true_login = "sky@gmail.com"
#
# true_password = "12345"
#
# user_login = input('Введите логин: ')
# user_password = input('Введите пароль: ')
#
# if user_login == true_login and user_password == true_password:
#     print("Вы вошли в систему")
# else:
#     print('Логин или пароль неверный')

# for i in range(15):
#     print('Купи слона!')

# k = 0
# for i in range(0, 101, 2):
#     k += i
# print(k)

# k = 1
# for i in range(5, 16):
#     k *= i
# print(k)


# num = int(input())
# x = 0
# for i in range(num + 1):
#     if i % 2 == 0:
#         x -= i
#     else:
#         x += i
# print(x)

#
# num = int(input('Введите нечетное число: '))
# for i in range(num + 1):
#     if i


# months = [
# 'январь', 'февраль', 'март', 'апрель',
# 'май', 'июнь', 'июль', 'август',
# 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
# ]
#
# # Продолжи решение ниже:
# winter = months[-1:] + months[0:2]
# spring = months[2:5] # Пример решения
# summer = months[5:8]
# autumn = months[8:11]
# print(f'Зима: {winter}')
# print(f'Весна: {spring}')
# print(f'Лето: {summer}')
# print(f'Осень: {autumn}')


# food = ['чебурек', 'огурец', 'сосиска']
# print(food)


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
# print(deals[0])
# print(deals[-1])


# deals = [
# 'погулять с друзьями',
# 'почитать новости и сцепиться с кем-нибудь в комментах',
# 'почитать книжку',
# 'рассмотреть потолок',
# 'поиграть в Brawl stars',
# 'помыть посуду',
# 'сказать родителям, что заболел',
# 'залипнуть в летсплеях по роблоксу'
# ]
# deals[int(input())] = input()
# print(deals)

# months = [
#   'январь', 'февраль', 'март', 'апрель',
#   'май', 'июнь', 'июль', 'август',
#   'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
# ]
#
# print(months[::-1])


# num = int(input('Введите число: '))
# a = 1
# for i in range(num + 1):
#     for j in range(i):
#         print(a * "*", end=' ')
#         a += 1
#         print()
#


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# newList = [i.upper() for i in keywords if len(i) >= 5]
# print(newList)


# items = [input(), input(), input() ]
# print(items)

# items = []
# flag = True
# while flag == True:
#     newList = items.append(input())
#     if newList == '':
#         break
# print(items)

# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
#
# # Допиши код везде, где стоит "..."
#
# while True:
#     newDeals = deals.pop(2)
#     if newDeals == '':
#         break
#     else:
#         ...
#         del deals[...]
#
# print(...)


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
# ]

# print(f'Не делать уроки, а {deals[0]}')
# print(f'Не делать уроки, а {deals[1]}')
# print(f'Не делать уроки, а {deals[2]}')
# print(f'Не делать уроки, а {deals[3]}')
# print(f'Не делать уроки, а {deals[4]}')
# print(f'Не делать уроки, а {deals[5]}')
# print(f'Не делать уроки, а {deals[6]}')
# print(f'Не делать уроки, а {deals[7]}')
# print(f'Не делать уроки, а {deals[8]}')


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
#     ]
#
# new_deals = []
# a = input(f'{deals[0]} - сделано? (да / нет):')
# if a == 'да':
#     deals.pop(0)
# else:
#     new_deals.append('погулять с друзьями')
# print(deals)
# print(new_deals)


# count = 0
# p = 0
# for i in range(1, 10):
#     x = int(input())
#     if x > 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(x)
#     print(p)
# else:
#     print('NO')




# word = input()
# l = ''
# d = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for sym in word:
#     for k, v in d.items():
#         if sym.upper() in v:



# answer = 'ok'
# num = '11111'
# for i in range(len(num) - 1):
#     if num[i] != num[i + 1]:
#         answer = 'no'
# print(answer)


# names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
# phones = ['-79899899889', '112', '1', '+09998765432', '0']
#
# book_phones = {
#
# }
# for index in range(len(names)):
#     book_phones[names[index]] = phones[index]
#
# print(book_phones)


# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# names = {}
# phones = {}
# for index in range (len(book_phones)):
#     # phones[]
#     print()


# d = {
#     'п': 'p',
#     'р': 'r',
#     'и': 'i',
#     'в': 'v',
#     'е': 'e',
#     'т': 't',
# }
#
# newWord = ''
# word = 'привет'
#
# for i in word:
#     if i in d:
#         newWord += d[i]
#     else:
#         newWord += i
#
# print(newWord)

# answer = 'False'
# w = 'Вижу зверей'
# d = 'Живу резвей'
#
# for i in w:
#     for j in d:
#         if i in j:
#             answer = 'True'
# print(answer)


# strings = ["как", "дела", "дела", "как", "как", "у тебя", "дела", "как", ":-O"]
# print(sorted(set(strings)))


# white_list = set()  # Множество, в котором будет храниться "белый список"
# answers = set()     # Множество будущих разрешенных ответов
#
# white_request = ' '   # Объявление переменной, через которую будут заноситься пункты белого списка
# request = ' '         # Объявление переменной, через которую будут заноситься пункты запросов учеников
#
#
# while white_request != '':
#   ...
#
#
# while request != '':
#   ...
#
#
# for answer in answers:
#   ...

# months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
# 'Декабрь')
#
# winter = months[-1:] + months[0:2]
# spring = months[2:5]
# summer = months[5:8]
# autumn = months[8:11]
#
# d, ya, f = winter
#
# half_year1, half_year2 = (winter, spring), (summer, autumn)
#
# print(d, ya, f)
# print(half_year1, half_year2)


# d = {
#     'а': 'a',
#     'б': 'b',
#     'в': 'v',
#     'г': 'g',
#     'д': 'd',
#     'е': 'e',
#     'ё': 'e',
#     'ж': 'zh',
#     'з': 'z',
#     'и': 'i',
#     'й': 'i',
#     'к': 'k',
#     'л': 'l',
#     'м': 'm',
#     'н': 'n',
#     'о': 'o',
#     'п': 'p',
#     'р': 'r',
#     'с': 's',
#     'т': 't',
#     'у': 'y',
#     'ф': 'f',
#     'х': 'kh',
#     'ц': 'ts',
#     'ч': 'ch',
#     'ш': 'sh',
#     'щ': 'shch',
#     'ъ': 'ъ',
#     'ы': 'ы',
#     'ь': '`',
#     'э': 'e',
#     'ю': 'u',
#     'я': 'ya',
# }



# w = 'Вижу зверей'
# nd1 = {}
# for i in w.lower():
#     if i.isalpha():
#         if i not in nd1:
#             nd1[i] = 0
#         nd1[i] += 1
# print(nd1)
# d = 'Живу резвей'
# nd2 ={}
# for j in d.lower():
#     if j.isalpha():
#         if j not in nd2:
#             nd2[j] = 0
#         nd2[j] += 1
# print(nd2)
# if nd2 == nd1:
#     print(True)
# else:
#     print(False)

# w = 'Когда увидимся'
# newD1 = {}
# for i in w.lower():
#     if i.isalpha():
#         if i not in newD1:
#             newD1[i] = 0
#         newD1[i] += 1
# print(newD1)
#
# d = 'тогда и свидимся'
# newD2 = {}
# for k in d.lower():
#     if k.isalpha():
#         if k not in newD2:
#             newD2[k] = 0
#         newD2[k] += 1
# print(newD2)
#
# if newD1 == newD2:
#     print(True)
# else:
#     print(False)


# w = 'qwerty! poiu?'
# d1 = {}
# for i in w.lower():
#     if i.isalpha():
#         if i not in d1:
#             d1[i] = 0
#         d1[i] += 1
#
# w2 = 'ertyqw ipou'
# d2 = {}
# for k in w2.lower():
#     if k.isalpha():
#         if k not in d2:
#             d2[k] = 0
#         d2[k] += 1
# print(d2)
# if d1 == d2:
#     print(True)
# else:
#     print(False)


# w = ' William Shakespeare'
# d1 = {}
# for i in w.lower():
#     if i.isalpha():
#         if i not in d1:
#             d1[i] = 0
#         d1[i] += 1
# print(d1)
#
# w2 = 'I am a weakish: speller,'
# d2 = {}
# for k in w2.lower():
#     if k.isalpha():
#         if k not in d2:
#             d2[k] = 0
#         d2[k] += 1
# print(d2)
#
# if d1 == d2:
#     print(True)
# else:
#     print(False)


# def find_all(string: str, symbol: str) -> list:
#     answer = []
#     for s in range(len(string)):
#         if symbol == string[s]:
#             answer.append(s)
#     return answer
#
#
# print(find_all('abcdabcdea', 'a'))


# def temp(C):
#     return C * 1.8 + 32
# print(temp(1))



# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']

# отфильтровать элементы длинна которых больше 4 символов и которые являются палиндромами
# палиндром - это слово которое одинаково читается как справа налево так и слева направо

# res = []
#
# for i in words:
#     if len(i) > 4 and i[::-1] == i:
#
#         res.append(i)
#
# print(res)


# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# filterData = filter(lambda citiinfo: citiinfo[1] > 15000000, data)
# # print(list(filterData))
#
# mapData = map(lambda citiinfo: citiinfo[0], filterData)
#
# print(list(mapData))


# import json
#
# with open('newFile.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=True)


# import json

# with open('file1.json', 'r', encoding='utf-8') as file1, open('file2.json', 'r', encoding='utf-8') as file2:
#     write = json.load(file1)
#     w2 = json.load(file2)
#
# for i in w2:
#
#     if i not in write:
#         write[i] = w2[i]
#
#     else:
#         if write[i][0] > w2[i][0]:
#             write[i] = w2[i]
#
#
#
# print(write)


# num = [0, 1, 1]
#
# for i in range(18):
#     num.append(num[-1] + num[-2])
#
# print(num)


# def recursion(n):
#     while n >= 1:
#         print(n)
#         n -= 1
#
# recursion(int(input('Число: ')))



# написать класс Gun, в котором будет реализован 1 метод shoot() при вызове этого метода на экрне мы должны видеть слово 'pif'
# при ПЕРВОМ вызове этого метода на экране мы должны видеть слово 'pif'
# при ВТОРОМ вызове этого метода на экране мы должны видеть слово 'paf'
# при ТРЕТЬЕМ вызове этого метода на экране мы должны видеть слово 'pif'
# при ЧЕТВЕРТОМ вызове этого метода на экране мы должны видеть слово 'paf' и тд.
# shots_reset() - метод который будет сбрасывать счетчик до нуля
# shots_count() - метод который будет возвращать количество выстрелов на текущий момент

# class Gun:
#     def __init__(self):
#         self.num = 0
#     def shots_reset(self):
#         self.num = 0
#     def shots_count(self):
#         return self.num
#
#     def shoot(self):
#         if self.num % 2 == 0:
#             print('pif')
#         else:
#             print('paf')
#
#         self.num += 1
#
# gun1 = Gun()
# print(gun1.shots_count())
#
# gun1.shoot()
# gun1.shoot()
# gun1.shots_reset()
# gun1.shoot()
# gun1.shoot()
# print(gun1.shots_count())

#
# def gaslighting(shirt_word:str, your_word:str, friends_letters:str) -> bool:
#
#     for w in range(len(shirt_word)):
#         if shirt_word[w] != your_word[w]:
#             if shirt_word[w] in friends_letters or your_word[w] in friends_letters:
#                 return True
#     return False
#
# print(gaslighting("snack", "snake", "c"))


# class BankAccount:
#
#     def __init__(self, balance=0):
#         self._belance = balance
#
#     def get_balance(self):
#         return self._belance
#
#     def deposit(self, amount):
#         self._belance += amount
#
#     def withdraw(self, amount):
#         if amount <= self._belance:
#             self._belance -= amount
#         else:
#             print("На счете недостаточно средств")
#
#     def transfer(self, account, amount):
#         if amount > self._belance:
#             print("На счете недостаточно средств")
#         else:
#             self._belance -= amount
#             account.deposit(amount)
#
# a = BankAccount()
#
# print(a.get_balance())
# a.deposit(100)
# print(a.get_balance())



# Нужно реализовать класс Book, описывающий книгу
# При создании экземпляра мы должны передавать 3 аргумента: название, автор, и год издания

# Формальное представление:
# Book('<название книги>', '<автор книги>', <год издания>)

# неформальное
# <название книги> (<автор книги>, <год выпуска книги>)

# class Book:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f'{self.name}, {self.author}, {self.year}'
#
#     def __repr__(self):
#         return f'Book("{self.name}", "{self.author}", {self.year})'



# task 1
#
# Преподаватель по математике проводит занятия по 45 минут с перерывами по 10 минут.
# Преподаватель обозначает время начала рабочего дня и время окончания рабочего дня.
# Напиши программу, которая генерирует и выводит расписание занятий.
#
# Формат входных данных
# На вход программе в первой строке подается время начала рабочего дня в формате HH:MM.
# В следующей строке вводится время окончания рабочего дня в том же формате.
#
# Формат выходных данных
# Программа должна сгенерировать и вывести расписание занятий.
# На первой строке выводится время начала и окончания первого занятия в формате HH:MM - HH:MM,
# на второй строке — время начала и окончания второго занятия в том же формате, и так далее.
#
# ------------------------------------------------------------------------------------------------------------------------
#
# task 2
#
# Во время решения очередной задачи программист фиксирует время начала и окончания ее решения и добавляет полученные
# результаты в список data.
# Каждый результат представляет собой кортеж, первым элементом которого является время начала решения в виде строки
# в формате HH:MM, вторым элементом — время окончания решения в виде строки в том же формате.
# Напиши код, который выведет общее целое количество минут, которое программист затратил на решение всех задач.
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# ------------------------------------------------------------------------------------------------------------------------
#
# task 3
#
# Даны две даты — левая и правая границы диапазона соответственно.
# Напиши программу, которая из этого диапазона, включая границы, выводит, начиная с даты,
# у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг=)
#
# Формат входных данных
# На вход программе подаются две даты в формате DD.MM.YYYY — левая и правая границы диапазона соответственно,
# каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна из указанного диапазона, включая концы, вывести, начиная с даты,
# у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.
# Даты должны быть расположены каждая на отдельной строке, в формате DD.MM.YYYY
#
# test input
# 01.11.2021
# 10.11.2021
#
# test output
# 02.11.2021
# 05.11.2021


# from datetime import datetime, timedelta
#
# st = '09:20'
# en = '13:40'
#
# dtStart = datetime.strptime(st, '%H:%M')
# dtEnd = datetime.strptime(en, '%H:%M')
# les = timedelta(minutes=45)
# lE = timedelta(minutes=10)
#
# while dtStart + les < dtEnd:
#     nl = dtStart + les
#     print(f'{dtStart.strftime("%H:%M")} - {nl.strftime("%H:%M")}')
#     dtStart += lE + les

# Во время решения очередной задачи программист фиксирует время начала и окончания ее решения и добавляет полученные
# результаты в список data.
# Каждый результат представляет собой кортеж, первым элементом которого является время начала решения в виде строки
# в формате HH:MM, вторым элементом — время окончания решения в виде строки в том же формате.
# Напиши код, который выведет общее целое количество минут, которое программист затратил на решение всех задач.

from datetime import datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

se = timedelta(minutes=0)
for start, end in data:
    s = datetime.strptime(start, '%H:%M')
    e = datetime.strptime(end, '%H:%M')

    se += e - s
print(se)



#!/usr/bin/env python3
# coding: utf-8
#
# первая строка позволяет запускать этот скрипт как ./intro.py, 
#   а не только через python3 intro.py, подробности: гуглите shebang 
# вторая строка задаёт кодировку в этом файле, для python3 по умолчанию
# utf-8, поэтому можно не указывать


### Intro:
# Python - multiparadigm language, dynamic typing
# Guido van Rossum
# Monty Python's Flying Circus
# PEPs (8 -- style guide, 20 -- Zen)
# Установка: sudo apt-get install python3
# Запуск: python3 <script_name>
# Интерактивная консоль: python3

# Рекомендумая среда разработки --- sublime_text_3
# View -> Indentation -> Tab width: 4
# View -> Intentation -> Indent using spaces 
# Запуск скрипта --- Ctrl-B

contact = {"name": "Андроник", "email": "andronik.ordian@gmail.com"}

email_format = "spbau/paradigms: {surname} {task_number}"
# Формат темы письма
print(email_format.format(surname="Pupkin", task_number=0))

# Исправление присылайте в том же письме
# Будет оцениваться корректность программы И качество кода
# Придерживайтесь одного стиля


### Variables, assignments
# #comment
# indentation

### Conditionals, braces are optional:

gpa = 5.0
if 4 < gpa < 4.5: # вместо && есть and, вместо || есть or
    skill = 'good'
elif gpa >= 4.5:
    skill = 'excellent'
else:
    skill = 'bad'

# # ternary
max_score = 1
score = 0.51
result = 'pass' if score > (0.5 * max_score) else 'fail'

### Functions
# def name(param, pampam):
#     """ Prints first parameter. """
#     print(param)

## Cycles
# while cond:
#   pass
# break, continue
def guess_number(secret=42):
    guess = None
    while True:
        # чтение числа из консоли и преобразование в int
        guess = int(input('Please enter a number: '))
        if guess == secret:
            print('Hooray')
            break # выход из цикла
        print('Another try')

# guess_number() # function call
# print(..)
# input(prompt)
# Help: help(<function_name>)

## Primitive types
# Dynamic typing
# Int, buit-in BigInt, 2 ** 6400
# float, 1e-10, 3.1415926
# complex (real + img i), complex(0, 1) ** 2
# strings -- immutable
# bool -- True, False

## Lists (c++ array or vector)
# Heterogeneous
empty_list = [] # or list()
xs = [1, 2, "3", 4.0] 
len(xs) # длина списка
# xs[i] -- получить i-ый элемент списка
# xs[i] = 2  # заменить i-ый элемент списка на 2
# xs[-1] -- последние элемент

# Slicing, срез -- взятие подсписка
# xs([start,] stop[, step]) -- общий синтаксис
# xs[:] - весь список (копия)
# xs[1:] - начиная с первого элемента (не включая нулевой)
# xs[:10] - до 10 (не включая)
# xs[1:10] - от 1 до 10
# xs[1:10:2] - от 1 до 10 с шагом 2
# xs[::-1] - в обратном порядке
# xs[ind1:in"d2] = lst2  - заменить подсписок на другой список
# xs.append(el), xs.remove(el), val in xs,
# xs.index(el), xs.count(el), xs.extend(list)
# список можно умножить на число
# [1,2,3] * 2 == [1,2,3, 1,2,3]
# ys = xs # aliasing
# Копирование
#   ys = xs.copy()
#   ys = xs[:]
#   ys = list(xs)
# Сортировка
# xs.sort() # изменяет xs
# xs.sort(reverse=True) # в обратном порядке
# def second(pair):
#     return pair[1]
# [("hello", 2), ("world", 1)].sort(key=second) # по 2-му элементу пары
# sorted(xs) ## новый список
# dir([]) - получить все методы (функции) над списками

# range([start,] stop[, step]) 
# синтаксис такой же как и у срезов
# for i in range(10):
#     print(i)
# for i in range(1, 10, 2):
#     pass
# list comprehensions
# Чтобы получить массив квадратов чисел в C++ вы пишите
# int result[100];
# for (int i = 0; i < 100; i++)
#     result[i] = i * i;

# В python вы пишите:
# [x * x for x in range(100)]
# Общий синтаксис с условием:
# [f(i) for i in list if condition]
# В python3 range не создаёт списка (O(1) памяти)
# Сам список можно получить так: list(range(100))

## for-each
# for var in sequence: # sequence is iterable
#   pass -- pass ничего не делает (заглушка)

### Strings, Строки
# ' ', " ", """ """,
# a = '''
#        Я помню чудное мгновенье,
#        Передо мной явилась ты,
#        ...
#     '''

# split(sep) --> help("".split)
# companies = ["apple", "google", "microsoft"]
# ', '.join(companies)
# separator.join(iterable)
# "".find(sustr)
# "".strip()
# a = 'hello'
# можно взять подстроку как и со списками (но нельзя изменять)
# Строки можно умножать
# 'a' * 4 == 'aaaa'
# По строке можно итерироваться
# for char in 'hello': 
#     pass

### Tuples
# Кортежи - это неизменяемые списки
# empty_tuple = (,)
# singleton = (1,)
# a = (1, 2, 3)
# a[0] = 2 # ошибка
# Неизменяемость кортежа означает, что нельзя заменить элемент
# Но если элемент изменяемый (например список), то его можно изменить
# a = ([1,2,3], 4)
# a[0].append(4)
# b = a
# a += (4, 5, 6) # можно изменить a, но предыдущий кортеж остался неизменным
# b != a


### Dictionaries - Словари - Map
# empty_dict = {} # or dict()
# capitals = dict(France='Paris',
#                 Germany='Berlin',
#                 Zimbabwe='Harare')
# capitals_2 = {'USA': 'Washington, D.C',
#               'Australia': 'Canberra',
#               'Russia': 'Moscow'}
# capitals_3 = dict([('Ireland', 'Dublin'), ('Poland', 'Warsaw')])
# capitals.update(capitals_2)
# capitals.update(capitals_3)

# capitals['Russia'] = 'Saint-Petersburg'
# len(capitals)
# print(capitals['Zimbabwe'])
# d.keys(), d.values(), d.items()
# for key in capitals:
#     print(key)
# for key, value in capitals.items():
#     print(key, ':', value)

# dict comprehensions
# {x: x * x for x in range(10) if x % 2 == 0}


### sets
# s = {1, 2,'hello'}
# 'hello' in s # True
# set comprehensions
# {i for i in range(1, 10, 2)}

### Files
# fd = open("intro.py", mode='r')
# Итерируемся по строкам файла
# for line in fd:
#   print(line)
# fd.close() # закрываем файл

# data = fd.read() # прочитать весь файл в строку

# HW
# https://www.dropbox.com/sh/l7zh2fquflldw9y/AAArxvYNcScTLqPJ5IL355EZa?dl=0

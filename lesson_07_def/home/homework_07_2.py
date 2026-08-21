# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити/доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True: # Виправлено: True (безкінечний цикл)
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > 25: # Виправлено: "  " -> " ", "25" -> 25 (str -> int)
            # Enter the action to take if the result is greater than 25
            break # Виправлено: pass (нічого не робити) -> break (припинити)
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1 # Виправлено: multi -> multiplier

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18 # (умова: надрукувати табличку множення до 25)
# 3x7=21 # (умова: надрукувати табличку множення до 25)
# 3x8=24 # (умова: надрукувати табличку множення до 25)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a, b):
    return a + b

# a = 1
# b = 2
# print(f"{a} + {b} = {sum_of_two_numbers(a, b)}") # 1 + 2 = 3


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3]
average = average(numbers)
print(average)  # (1 + 2 + 3) : 3 = 2 // Результат ділення float 2.0


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reversed_text(line):
    return line[::-1]

line = 'Hello'
print(reversed_text(line)) # olleH


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    if not words:
        return ""
    else:
        longest_word = words[0] # Найдовше слово в списку перше з індексом [0]
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
        return longest_word

words = ['apple', 'banana', 'cherry']
longest_word = find_longest_word(words)
print(longest_word)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    if index == -1:
        return -1
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
"""
Lesson_06
# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

password = input("Введіть пароль: ")
if len(password) >= 8:
    print("Вірно. Пароль містить принаймні 8 символів.")
else:
    print("Пароль повинен містити принаймні 8 символів.")
"""

def validate_password():
    """
    Функція запитує пароль, перевіряє чи пароль містить
    принаймні 8 символів і виводить результат перевірки.
    """
    password = input("Введіть пароль: ")
    if len(password) >= 8: # True якщо пароль валідний, False якщо ні
        print("Вірно. Пароль містить принаймні 8 символів.")
    else:
        print("Помилка. Пароль занадто короткий.")

validate_password()


# task 8
"""
Lesson_04
"""
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
'''
# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Завдання 1")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("Завдання 2")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print("Завдання 3")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)
'''

def clean_text(text):
    """ Послідовна очистка тексту"""
    text = text.replace("\n", " ") # заміна нових рядків на пробіл
    text = text.replace("....", " ") # заміна .... на пробіл
    text = " ".join(text.split()) # розбиває рядок на слова, обєднує пробілом
    return text

print(clean_text(adwentures_of_tom_sawer))


# task 9
'''
Lesson_05
# task 3. Перевірте, чи є в списку big_list дублікати
'''
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
'''
if len(big_list) == len(set(big_list)): # 10 != 9
    print("Дублікатів немає")
else:
    print("Є дублікати") # Є дублікати
'''

def has_duplicates(items):
    """ Перевіряє чи є дублікати в списку і виводить результат"""
    if len(items) == len(set(items)):
        print("Дублікатів немає")
    else:
        print("Є дублікати")

has_duplicates(big_list)

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
'''
Lesson_05
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key, value in base_dict.items():
    sum_dict[key] = value
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print(sum_dict) # {'contry': 'Ukraine', 'continent': 'Europe', 'size': '12312', 'a': 1, 'b': 2, 'c': 2, 'd': 3}
'''
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123} # Lesson_05 task 4
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12} # Lesson_05 task 4

# Об'єднання даних (об'єднання інформації клієнтів)
def merging_two_dictionaries(dictionarie_old, dictionarie_new):
    """
    Об'єднує два словника старий(базовий) і новий(доданий)
    в об'єднаний словник і якщо дані збігаються, то
    перетворює значення в строку і обєднує їх.
    """
    sum_dict = dictionarie_old.copy()
    print(f"Копіює старий словник в об'єднаний словник: \n{sum_dict}")
    # Копіює старий словник в об'єднаний словник: {'contry': 'Ukraine',
    # 'continent': 'Europe', 'size': 123}
    for key, value in dictionarie_new.items():
        if key in sum_dict: # якщо ключ є в об'єднаному словнику
            sum_dict[key] = f"{sum_dict[key]} {value}"
            print(f"Об'єднує існуючі ключі: \n{sum_dict}")
            # Об'єднує існуючі ключі:
            # {'contry': 'Ukraine', 'continent': 'Europe',
            # 'size': '123 12', 'a': 1, 'b': 2, 'c': 2, 'd': 3}
        else: # якщо ключа немає в об'єднаному словнику
            sum_dict[key] = value # додає в sum_dict
            print(f"Додає новий ключ до старого словника: \n{sum_dict}")
            # Додає новий ключ до старого словника:
            # {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123,
            # 'a': 1, 'b': 2, 'c': 2, 'd': 3}
    return sum_dict

print(f"Обєднаний словник: \n{merging_two_dictionaries(base_dict, add_dict)}")
# Обєднаний словник: 
# {'contry': 'Ukraine', 'continent': 'Europe', 'size': '123 12', 'a': 1, 'b': 2,
# 'c': 2, 'd': 3}

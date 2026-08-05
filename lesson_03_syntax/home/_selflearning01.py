# Завдання для самоперевірки - Основи Python
# 10 завдань з автоматичними тестами

print("=== ЗАВДАННЯ ДЛЯ САМОПЕРЕВІРКИ ===\n")

# ЗАВДАННЯ 1: Створіть змінні для особистих даних
print("Завдання 1: Створіть змінні з вашими даними")
print("Створіть змінні: student_name, student_age, is_enrolled, gpa_score")
print("Приклад: student_name = 'Іван Петров'")

# Ваш код тут:
student_name = "Tetiana"  # Замініть на ваше ім'я
student_age = 46          # Замініть на ваш вік
is_enrolled = True        # Замініть на True якщо навчаєтеся
gpa_score = 100.0         # Замініть на ваш середній бал

# ЗАВДАННЯ 2: Арифметичні операції
print("\nЗавдання 2: Виконайте арифметичні операції")
print("Обчисліть результати операцій з числами 25 та 4")

# Ваш код тут:
addition_result = 25 + 4        # 25 + 4
subtraction_result = 25 - 4     # 25 - 4
multiplication_result = 25 * 4  # 25 * 4
division_result = 25 / 4        # 25 / 4
floor_division_result = 25 // 4 # 25 // 4
modulo_result = 25 % 4          # 25 % 4
power_result = 25 ** 4          # 25 ** 4

# ЗАВДАННЯ 3: Робота з рядками
print("\nЗавдання 3: Обробіть рядок 'Python Programming Language'")
text = "Python Programming Language"

# Ваш код тут:
first_char = text[0]           # Перший символ
last_char = text[-1]           # Останній символ
text_length = len(text)        # Довжина рядка
first_word = text[0:6]         # Перше слово (індекси 0-5)
last_word = text[19:27]        # Останнє слово (індекси 19-26)

# ЗАВДАННЯ 4: Форматування рядків
print("\nЗавдання 4: Створіть форматовані рядки")
name = "Марія"
age = 22
height = 1.65

# Ваш код тут (використайте f-strings):
greeting = f"Привіт, мене звати {name}"  # "Привіт, мене звати Марія"
age_info = f"Мені {age} роки"            # "Мені 22 роки"
height_info = f"Мій зріст {height} м"    # "Мій зріст 1.65 м"

# ЗАВДАННЯ 5: Конвертація типів
print("\nЗавдання 5: Конвертуйте типи даних")
str_number = "123"
str_float = "45.67"
number = 89

# Ваш код тут:
converted_int = int(str_number)       # str_number у int
converted_float = float(str_float)    # str_float у float
converted_str = str(number)           # number у str

# ЗАВДАННЯ 6: Математичні обчислення
print("\nЗавдання 6: Обчисліть площу та периметр прямокутника")
width = 12.5
height = 8.3

# Ваш код тут:
rectangle_area = width * height            # width * height
rectangle_perimeter = 2 * (width + height) # 2 * (width + height)

# ЗАВДАННЯ 7: Робота з індексами
print("\nЗавдання 7: Витягніть символи з рядка за індексами")
sample_text = "Programming"

# Ваш код тут:
char_at_0 = sample_text[0]           # Символ на позиції 0
char_at_5 = sample_text[5]           # Символ на позиції 5
char_at_minus_1 = sample_text[-1]    # Останній символ (індекс -1)
char_at_minus_3 = sample_text[-3]    # Третій з кінця (індекс -3)

# ЗАВДАННЯ 8: Зрізи рядків
print("\nЗавдання 8: Створіть зрізи рядка")
full_text = "Hello World Python"

# Ваш код тут:
first_five = full_text[0:5]          # Перші 5 символів
middle_part = full_text[6:11]        # Символи з 6 по 10 включно
last_six = full_text[-6:]            # Останні 6 символів
every_second = full_text[::2]        # Кожен другий символ

# ЗАВДАННЯ 9: Логічні операції
print("\nЗавдання 9: Виконайте логічні операції")
a = True
b = False
c = True

# Ваш код тут:
and_result = False       # a and b
or_result = True        # a or b
not_result = False        # not a
complex_result = True   # (a and c) or (not b)

# ЗАВДАННЯ 10: Складні обчислення
print("\nЗавдання 10: Обчисліть складний вираз")
x = 10
y = 3
z = 2

# Ваш код тут:
result1 = (x + y) * z             # (x + y) * z
result2 = x ** y - z              # x ** y - z
result3 = (x / y) + (z * 2)       # (x / y) + (z * 2)
result4 = x % y + z ** 2          # x % y + z ** 2

print("\n=== ЗАКІНЧІТЬ ВИКОНАННЯ ЗАВДАНЬ І ЗАПУСТІТЬ ТЕСТИ ===")
# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements = set(small_list)
# print(unique_elements) # {1, 2, 3, 4, 5}
for element in unique_elements:
    print(element)
'''
1
2
3
4
5
'''

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = sum(small_list) / len(small_list)
print(average) # 3.2857142857142856

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
if len(big_list) == len(set(big_list)): # 10 != 9
    print("Дублікатів немає")
else:
    print("Є дублікати") # Є дублікати

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

key_for_max_value = None
values_tuple = tuple(add_dict.values()) # (1, 2, 2, 3, 12)
value_max = max(values_tuple) # 12

for key, value in add_dict.items():
    if value == value_max:
        key_for_max_value = key
print(key_for_max_value) # size

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
keys = base_dict.values()
values = base_dict.keys()
dict_from_pairs = dict(zip(keys, values))
print(dict_from_pairs) # {'Ukraine': 'contry', 'Europe': 'continent', 123: 'size'}

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

# task 7.
line = "Створіть список з всіх символів, які входять у заданий рядок"
chars_list = list(line)
print(chars_list) # ['С', 'т', 'в', 'о', 'р', 'і', 'т', 'ь', ' ', 'с', 'п', 'и', 'с', 'о', 'к', ' ', 'з', ' ', 'в', 'с', 'і', 'х', ' ', 'с', 'и', 'м', 'в', 'о', 'л', 'і', 'в', ',', ' ', 'я', 'к', 'і', ' ', 'в', 'х', 'о', 'д', 'я', 'т', 'ь', ' ', 'у', ' ', 'з', 'а', 'д', 'а', 'н', 'и', 'й', ' ', 'р', 'я', 'д', 'о', 'к']

# task 8. Обчисліть суму елементів двох змінних через sum()
value_1 = [1, 2, 3, 4, 5] # список
value_2 = (4, 6, 5, 10) # кортеж
total_sum = sum(value_1) + sum(value_2)
print(total_sum) # 40

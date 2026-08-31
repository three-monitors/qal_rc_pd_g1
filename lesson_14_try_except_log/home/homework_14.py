"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(string_list: list, raise_errors=True):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою.

    Параметр raise_errors:
    - True: викликає ValueError для некоректних даних (для тестів)
    - False: обробляє помилки всередині функції (для демонстрації)
    """

    # Перевірка, чи передано список
    if not isinstance(string_list, list):
        if raise_errors:
            raise ValueError("Вхідні дані мають бути списком")
        else:
            return "Помилка: Вхідні дані мають бути списком"

    # Перевірка на порожній список
    if len(string_list) == 0:
        if raise_errors:
            raise ValueError("Список не може бути порожнім")
        else:
            return "Помилка: Список не може бути порожнім"

    result = []
    for item in string_list:
        try:
            # Перевірка, чи елемент є рядком
            if not isinstance(item, str):
                raise AttributeError("Елемент не є рядком")

            # Розділення рядка на числа
            numbers = item.split(",")

            # Конвертація в числа та підрахунок суми
            total = 0
            for num in numbers:
                total += int(num.strip())

            result.append(total)

        except (ValueError, AttributeError) as e:
            if isinstance(e, AttributeError):
                result.append("Не можу це зробити! AttributeError")
            else:
                result.append("Не можу це зробити!")

    return result


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)  # [6, 10]

    # output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    # print(output)

    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])
    print(output)  # [6, "Не можу це зробити!", 10]

    output = sum_numbers_in_list(["1,2,3,4", 7])
    print(output)  # [10, "Не можу це зробити! AttributeError"]

    output = sum_numbers_in_list([], raise_errors=False)
    print(output)

    output = sum_numbers_in_list("21", raise_errors=False)
    print(output)

    # sum_numbers_in_list([])  # ValueError
    # sum_numbers_in_list("21")  # ValueError

    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """

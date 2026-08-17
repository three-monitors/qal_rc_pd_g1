# Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
import os
with open("hello.txt", "w") as file:
    file.write("Hello, Python!")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with open("hello.txt", "a") as file:
    file.write("\nLearning file operations.")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open("hello.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() видаляє \n

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with open("hello.txt", "r") as file:
    content = file.read()
    print(f"Кількість символів: {len(content)}")

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here

# Створення папки
os.makedirs("data", exist_ok=True)

# Створення файлу всередині
with open("data/notes.txt", "w") as file:
    file.write("My first note.")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here

# Список файлів у папці
files = os.listdir("data")
print("Файли в папці data:", files)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
with open("data/notes.txt", "r") as source:
    content = source.read()

with open("data/copy.txt", "w") as destination:
    destination.write(content)

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
with open("a.txt", "w") as file:
    file.write("Content from file A")

with open("b.txt", "w") as file:
    file.write("Content from file B")

with open("a.txt", "r") as file_a, open("b.txt", "r") as file_b:
    content_a = file_a.read()
    content_b = file_b.read()

with open("ab.txt", "w") as file:
    file.write(content_a + content_b)

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
with open("data/notes.txt", "r") as file:
    content = file.read()
    if "note" in content:
        print("Знайдено")
    else:
        print("Не знайдено")

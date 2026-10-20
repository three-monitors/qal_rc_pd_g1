import itertools
import random


# Завдання 1: Ітератор «Ланцюжок доручень»
class ChainOfOrders:
    """Ітератор ланцюжка доручень"""

    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):  # Реалізувати методи `__iter__()`..
        return self

    def __next__(self):  # ..та `__next__()`
        if self.index >= len(self.names):
            raise StopIteration  # Якщо список порожній — одразу `StopIteration`

        current_name = self.names[self.index]

        # Якщо це останній елемент
        if self.index == len(self.names) - 1:
            self.index += 1
            return f"{current_name} каже: теля прив'язав!"

        # Якщо це не останній елемент
        next_name = self.names[self.index + 1]
        self.index += 1
        return f"{current_name} каже {next_name}: передай далі!"


# Завдання 2: Генератор «Чутка по селу»
def village_rumor(start_message, people):  # параметри: початкове повідомлення, список імен
    """Генератор чутки по селу"""
    accumulated_additions = ""

    for i, person in enumerate(people):
        is_first = (i == 0)
        is_last = (i == len(people) - 1)
        
        if is_first:
            # Перша ітерація: повертає оригінальне повідомлення від першої людини
            yield f"{person} каже: \"{start_message}\""
        elif is_last:
            # Остання людина додає `"(і всі дізналися!)"` замість звичайного переказу
            if len(people) > 1:
                accumulated_additions += f" (переказала {people[i-1]})"
            yield f"{person} переказує: \"{start_message}{accumulated_additions} (і всі дізналися!)\""
        else:
            # Кожна наступна: людина «переказує по-своєму» — додає в кінець повідомлення `"(переказав <ім'я>)"`
            accumulated_additions += f" (переказала {people[i-1]})"
            yield f"{person} переказує: \"{start_message}{accumulated_additions}\""


# Завдання 3: Генераторний вираз «Скільки разів передали»
def count_transfer_events(events):
    """Підраховує події передачі доручення через генераторний вираз"""
    return sum(1 for event in events if "передав доручення" in event)


# Завдання 4: Нескінченний генератор «Черга на толоці»
def toloka_queue(workers):
    """Нескінченний генератор черги на толоці"""
    while True:
        for worker in workers:
            yield f"Черга: {worker}"


# Завдання 5: «Де загубилось теля?» — ліниве читання
def find_calf(log):  # приймає будь-який ітерований об'єкт `log` (список рядків або файл)
    """Генератор для пошуку першого рядка з прив'язуванням теля"""
    for line in log:  # по одному переглядає рядки
        if "прив'язав" in line or "прив'язала" in line:  # як тільки знаходить рядок, що містить слово `"прив'язав"` або `"прив'язала"`
            yield line  # повертає його через `yield`
            break  # зупиняється / після першого знайденого


# Бонус: Клас-ітератор «Телефон»
class TelephoneChain:
    """Ітератор зламаного телефону з випадковими перекручуваннями"""

    def __init__(self, names, message):
        self.names = names
        self.message = message
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.names):
            raise StopIteration

        current_name = self.names[self.index]

        # З імовірністю 30% перекручуємо одне слово
        if random.random() < 0.3:
            words = self.message.split()
            if words:
                random_index = random.randint(0, len(words) - 1)
                words[random_index] = "???"
                self.message = " ".join(words)

        self.index += 1
        return (current_name, self.message)


# Приклади використання для тестування
if __name__ == "__main__":
    # Завдання 1
    print("=== Завдання 1: Ланцюжок доручень ===")
    chain = ChainOfOrders(["Дід", "Батько", "Михайлик", "Василько"])
    for message in chain:  # Клас має працювати у циклі `for`
        print(message)
        # Дід каже Батько: передай далі!
        # Батько каже Михайлик: передай далі!
        # Михайлик каже Василько: передай далі!
        # Василько каже: теля прив'язав!
    print("\n")

    # Завдання 2
    print("=== Завдання 2: Чутка по селу ===")
    for version in village_rumor("Теля втекло!", ["Горпина", "Параска", "Явдоха", "Оксана"]):
        print(version)
        # Горпина каже: "Теля втекло!"
        # Параска переказує: "Теля втекло! (переказала Горпина)"
        # Явдоха переказує: "Теля втекло! (переказала Горпина) (переказала Параска)"
        # Оксана переказує: "Теля втекло! (переказала Горпина) (переказала Параска) (і всі дізналися!)"

    print("\n")

    # Завдання 3
    print("=== Завдання 3: Скільки разів передали ===")
    events = [
        "Михайлик передав доручення",
        "Василько відмовився",
        "Грицько передав доручення",
        "Оленка прив'язала теля",
        "Данилко передав доручення",
    ]

    # Генераторний вираз: фільтруємо + витягуємо імена + підраховуємо
    count = sum(1 for event in events if "передав доручення" in event)  # count = sum(...)
    # або
    # count = count_transfer_events(events)
    print(f"Доручення передавали {count} рази")
    # Доручення передавали 3 рази

    print("\n")

    # Завдання 4
    print("=== Завдання 4: Черга на толоці ===")
    queue = toloka_queue(["Іван", "Марія", "Степан"])
    for turn in itertools.islice(queue, 7):  # Взяти перші 7 чергувань
        print(turn)
        # Черга: Іван
        # Черга: Марія
        # Черга: Степан
        # Черга: Іван
        # Черга: Марія
        # Черга: Степан
        # Черга: Іван

    print("\n")

    # Завдання 5
    print("=== Завдання 5: Де загубилось теля? ===")
    journal = [
        "Михайлик отримав доручення",
        "Михайлик передав Василькові",
        "Василько загрався",
        "Василько передав Оленці",
        "Оленка прив'язала теля біля хліва",
        "Оленка пішла додому",
        "Дід заспокоївся",
    ]
    result = next(find_calf(journal))  # використай `next()` щоб отримати лише перший результат
    print(result)
    # Оленка прив'язала теля біля хліва

    print("\n")

    # Бонус
    print("=== Бонус: Телефон ===")
    phone = TelephoneChain(
        ["Андрій", "Богдан", "Володимир"], "Привіт, як справи?")
    for name, message in phone:
        print(f"{name}: {message}")
        # Андрій: Привіт, як справи? / 'Привіт'|'???' , & 'як'|'???' & 'справи'|'???' / random(0..3)
        # Богдан: Привіт, як справи? / 'Привіт'|'???' , & 'як'|'???' & 'справи'|'???' / random(0..3)
        # Володимир: Привіт, як справи? / 'Привіт'|'???' , & 'як'|'???' & 'справи'|'???' / random(0..3)

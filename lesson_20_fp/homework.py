from functools import reduce


# Завдання 1 — Зарплати
def task1_salaries():
    """Знаходить суму зарплат, що перевищують 35000 грн, після підвищення на 10%"""
    salaries = [30000, 45000, 28000, 60000, 52000, 33000]

    # 1. Підвищення на 10%
    raised = list(map(lambda s: s * 1.1, salaries))
    print(f"Підвищені зарплати на 10%: {raised}")

    # 2. Тільки більше 35000
    high = list(filter(lambda s: s > 35000, raised))
    print(f"Зарплати > 35000: {high}")

    # 3. Сума
    total = reduce(lambda acc, s: acc + s, high, 0)

    print(f"Сума: {total:.2f} грн.")  # Сума: 228700.00 грн


# Завдання 2 — Слова
def task2_words():
    """Знаходить унікальні слова, довші за 4 символи, в алфавітному порядку"""
    text = "Python це потужна мова програмування яка підходить для різних задач"

    # Розбити на слова
    words = text.split()
    print(f"Всі слова: {words}")

    # Тільки довші за 4 символи, в нижньому регістрі, без дублів
    long_unique = sorted(
        set(filter(lambda w: len(w) > 4, map(str.lower, words))))

    print(
        f"Слова > 4 символів: {list(filter(lambda w: len(w) > 4, map(str.lower, words)))}")
    print(f"Унікальні слова: {long_unique}")


def main():
    """Демонстрація обох завдань"""
    print("=== Завдання 1 — Зарплати ===")
    task1_salaries()

    print("\n=== Завдання 2 — Слова ===")
    task2_words()


if __name__ == "__main__":
    main()

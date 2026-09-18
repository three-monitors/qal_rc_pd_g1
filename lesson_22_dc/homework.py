from functools import reduce


# Завдання 1: Охоронці воріт
def is_strong(password):
    """Перевіряє чи пароль надійний"""
    if len(password) < 8 or len(password) > 20:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if ' ' in password:
        return False
    return True


def task1_passwords():
    """Перевірка паролів"""
    passwords = [
        "Cossack1",
        "sich",
        "ZAPORIZHZHIA2024",
        "Sich Gate 5",
        "Mazepa99",
        "короткий1",
        "BohunTheBrave",
        "D0br0nich!",
        "ааааааА1",
        "Valid1Pass",
    ]

    # Надійні паролі
    strong = list(filter(lambda p: is_strong(p), passwords))
    print("Надійні паролі:")
    for p in strong:
        print(f"✅ {p} — надійний")

    # Ненадійні паролі
    weak = list(filter(lambda p: not is_strong(p), passwords))
    print("\nНенадійні паролі:")
    for p in weak:
        print(f"❌ {p} — відхилено")


# Завдання 2: Перепис козацького реєстру
def task2_registry():
    """Обробка козацького реєстру"""
    raw_registry = [
        "  іван сірко  | полковник | 150",
        "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
        "петро дорошенко|сотник|75",
        "  Іван Мазепа | гетьман | 30000 ",
        "семен палій  |  полковник  | 500",
        "  Григорій Сковорода | філософ | 0",
    ]

    # Парсинг рядків
    def parse_row(row):
        parts = [p.strip() for p in row.split('|')]
        return {
            "name": parts[0].title(),
            "rank": parts[1].title(),
            "warriors": int(parts[2])
        }

    parsed = list(map(parse_row, raw_registry))

    # Фільтруємо лише з воїнами > 0
    with_warriors = list(filter(lambda r: r["warriors"] > 0, parsed))

    # Підрахунок загальної кількості воїнів
    total_warriors = reduce(lambda acc, r: acc +
                            r["warriors"], with_warriors, 0)

    # Сортування за кількістю воїнів (спадання)
    sorted_by_warriors = sorted(
        with_warriors, key=lambda r: r["warriors"], reverse=True)

    # Вивід таблиці
    print(f"Козацький реєстр ({len(sorted_by_warriors)} записів):")
    print("─" * 50)
    print(" №  Ім'я                 Посада       Воїни")
    print("─" * 50)
    for i, record in enumerate(sorted_by_warriors, 1):
        print(
            f" {i}  {record['name']:<20} {record['rank']:<12} {record['warriors']}")
    print("─" * 50)
    print(f"Разом воїнів: {total_warriors}")


# Завдання 3: Пошук козацьких шифрів
def is_palindrome(s):
    """Перевіряє чи рядок є паліндромом"""
    # Видаляємо пробіли і переводимо в нижній регістр
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]


def task3_palindromes():
    """Пошук паліндромів"""
    messages = [
        "А роза упала на лапу азора",
        "Козак",
        "Зараз",
        "level",
        "Python",
        "А баба",
        "racecar",
        "Запоріжжя",
        "noon",
        "Мазепа",
    ]

    # Знаходимо всі паліндроми
    palindromes = list(filter(lambda m: is_palindrome(m), messages))

    # Перетворюємо кожен паліндром у форматований рядок
    formatted = list(
        map(lambda p: f"🔐 {p} → {''.join(p.lower().split())}", palindromes))

    print("Знайдені шифри:")
    for f in formatted:
        print(f)


def main():
    """Демонстрація всіх завдань"""
    print("=== Завдання 1: Охоронці воріт ===")
    task1_passwords()

    print("\n=== Завдання 2: Перепис козацького реєстру ===")
    task2_registry()

    print("\n=== Завдання 3: Пошук козацьких шифрів ===")
    task3_palindromes()


if __name__ == "__main__":
    main()

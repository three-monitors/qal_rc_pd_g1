from pathlib import Path
from typing import Callable, Tuple


# Завдання 1: Козацька фабрика вітань
def make_greeter(rank: str) -> Callable[[str], str]:
    """Повертає функцію-вітальник для козаків"""
    def greeter(name: str) -> str:
        return f"{rank} {name}, слава Україні!"
    return greeter


# Завдання 2: Лічильник козацьких перемог
def make_battle_counter(warrior_name: str) -> Tuple[Callable, Callable, Callable]:
    """Повертає три функції для керування лічильником перемог"""
    victories = 0
    defeats = 0

    def add_victory() -> int:
        nonlocal victories
        victories += 1
        return victories

    def add_defeat() -> int:
        nonlocal defeats
        defeats += 1
        return defeats

    def get_stats() -> str:
        return f"Козак {warrior_name}: перемог — {victories}, поразок — {defeats}"

    return add_victory, add_defeat, get_stats


# Завдання 3: Сортування дружини
def make_sorter(field: str, reverse: bool = False) -> Callable:
    """Повертає функцію сортування для козаків"""
    def sorter(items):
        return sorted(items, key=lambda x: x[field], reverse=reverse)
    return sorter


# Бонус: Перевірник даних
def make_validator(field: str, min_val: int, max_val: int) -> Callable:
    """Повертає функцію-валідатор для перевірки даних"""
    def validator(data: dict) -> bool:
        if field not in data:
            return False
        value = data[field]
        return min_val <= value <= max_val
    return validator


def main():
    """Демонстрація всіх козацьких завдань"""
    print("=== Завдання 1: Козацька фабрика вітань ===")
    greet_hetman = make_greeter("Гетьман")
    print(greet_hetman("Іван Мазепа"))
    # Гетьман Іван Мазепа, слава Україні!

    greet_koshoviy = make_greeter("Кошовий отаман")
    print(greet_koshoviy("Богдан Хмельницький"))
    # Кошовий отаман Богдан Хмельницький, слава Україні!

    print("\n=== Завдання 2: Лічильник козацьких перемог ===")
    add_victory, add_defeat, get_stats = make_battle_counter("Тарас Бульба")

    print(add_victory())    # 1
    print(add_victory())    # 2
    print(add_defeat())     # 1
    print(get_stats())      # Козак Тарас Бульба: перемог — 2, поразок — 1

    print("\n=== Завдання 3: Сортування дружини ===")
    warriors = [
        {"name": "Тарас", "rank": "Сотник", "battles": 15},
        {"name": "Остап", "rank": "Козак", "battles": 8},
        {"name": "Богдан", "rank": "Сотник", "battles": 22},
        {"name": "Микола", "rank": "Кошовий", "battles": 30},
    ]

    sort_by_battles = make_sorter("battles", reverse=True)
    result = sort_by_battles(warriors)
    for warrior in result:
        print(
            f"{warrior['name']} — {warrior['rank']} — {warrior['battles']} битв")

    # Микола — Кошовий — 30 битв
    # Богдан — Сотник — 22 битв
    # Тарас — Сотник — 15 битв
    # Остап — Козак — 8 битв

    print("\n=== Бонус: Перевірник даних ===")
    validate_battles = make_validator("battles", 1, 50)
    print(validate_battles({"name": "Тарас", "battles": 15}))  # True
    print(validate_battles({"name": "Дід", "battles": 99}))    # False

    validate_rank = make_validator("battles", 0, 100)  # Для іншого поля
    print(validate_battles({"name": "Тарас", "battles": 0}))   # False


if __name__ == "__main__":
    main()

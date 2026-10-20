import csv
from pathlib import Path
from typing import List, Dict, Tuple


def read_file(filepath: Path) -> list[Dict]:
    """Зчитує один CSV-файл, повертає список словників"""
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(filepath: Path, content: list[Dict]) -> None:
    """Записує список словників у файл (з заголовкома)"""
    if not content:
        print("Немає даних для запису")
        return

    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content[0].keys())
        writer.writeheader()
        writer.writerows(content)


def find_duplicates(rows: List[Dict]) -> Tuple[List[Dict], int]:
    """Повертає (унікальні рядки, кількість дублікатів)"""
    seen = set()
    unique_rows = []
    duplicate_count = 0

    for row in rows:
        # Перетворюємо словник на tuple для порівняння
        row_tuple = tuple(sorted(row.items()))

        if row_tuple in seen:
            duplicate_count += 1
        else:
            seen.add(row_tuple)
            unique_rows.append(row)

    return unique_rows, duplicate_count


def main() -> None:
    """
    Чого не вистачає — основна логіка
    Задача — знайти та прибрати дублікати. Ця логіка ще не написана
    """
    """Координує все: читає, дедублікує, пише, виводить статистику"""

    # Шляхи до файлів
    file1 = Path(__file__).parent / "users_1.csv"
    file2 = Path(__file__).parent / "users_2.csv"
    output_file = Path(__file__).parent / "clean_users_3.csv"

    # Читаємо обидва файли
    data1 = read_file(file1)
    data2 = read_file(file2)

    print(f"Зчитано з {file1.name}: {len(data1)} записів")
    print(f"Зчитано з {file2.name}: {len(data2)} записів")

    # Об'єднуємо дані
    all_data = data1 + data2
    print(f"Всього записів: {len(all_data)}")

    # Шукаємо дублікати і отримуємо унікальні рядки
    unique_rows, duplicate_count = find_duplicates(all_data)

    # Записуємо унікальні рядки у файл
    write_csv(output_file, unique_rows)

    # Виводимо статистику
    print(f"Знайдено дублікатів: {duplicate_count}")
    print(f"Унікальних записів збережено: {len(unique_rows)}")
    print(f"Файл: {output_file}")


if __name__ == "__main__":
    main()

    # my_csv = Path(__file__).parent / "users_1.csv"
    # content = read_file(my_csv)
    # print(content, type(content))
    # my_csv_2 = Path(__file__).parent / "new2.csv"
    # write_csv(my_csv_2, content)

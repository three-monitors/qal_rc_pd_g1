import json
import os
from typing import List, Dict, Optional

# Визначаємо директорію
LESSON_DIR = os.path.dirname(os.path.abspath(__file__))

# Завдання 1: Серіалізація вручну


def task1_serialization():
    """Перевірка серіалізації вручну"""
    record = {
        "title": "Ой у лузі червона калина",
        "genre": "пісня",
        "region": "Полтавщина",
        "narrator": "Ганна Остапенко",
        "year": 1932,
        "content": "Красива дівчина з червоним вінком",
        "tags": ["калина", "вінок", "дівчина"],
        "verified": True
    }

    # 1. Перетворити на JSON-рядок
    json_str = json.dumps(record)
    print("1. JSON рядок:")
    print(json_str)
    print(f"Тип: {type(json_str)}")

    # 2. JSON з відступами та кирилицею
    json_formatted = json.dumps(record, indent=4, ensure_ascii=False)
    print("\n2. JSON з відступами:")
    print(json_formatted)

    # 3. Відновити об'єкт з рядка
    restored = json.loads(json_str)
    print(f"\n3. Відновлений об'єкт: {type(restored)}")
    print(f"Кількість полів: {len(restored)}")


# Завдання 2: Архів експедиції
def task2_archive():
    """Архів експедиції — запис і читання файлу"""
    records = [
        {
            "title": "Ой у лузі червона калина",
            "genre": "пісня",
            "region": "Полтавщина",
            "narrator": "Ганна Остапенко",
            "year": 1932,
            "content": "Красива дівчина з червоним вінком",
            "tags": ["калина", "вінок", "дівчина"],
            "verified": True
        },
        {
            "title": "Ой у лузі червона калина похилилася",
            "genre": "козацька балада",
            "region": "Харківщина",
            "narrator": "Мокрина Куличка",
            "year": 1885,
            "content": "Давній козацький варіант (основа «Розлилися круті бережечки»), записаний експедицією Миколи Лисенка",
            "tags": ["козаки", "калина", "журба"],
            "verified": True
        },
        {
            "title": "Ой у лузі червона калина похилилася",
            "genre": "стрілецька пісня",
            "region": "Волинь",
            "narrator": "Настя Селегейна",
            "year": 1943,
            "content": "Повстанський варіант з доповненими куплетами про батька, що ховав сина-стрільця",
            "tags": ["стрільці", "війна", "батько", "син"],
            "verified": True
        },
        {
            "title": "Ой у лузі калина стояла",
            "genre": "весільно-обрядова пісня",
            "region": "Катеринославщина",
            "narrator": "Олена Дубовик",
            "year": 1952,
            "content": "Ранковий весільний обряд умивання нареченої біля криниці, де образ калини символізує дівочу цноту",
            "tags": ["весілля", "криниця", "калина", "молода"],
            "verified": True
        },
        {
            "title": "Ой у лузі червона калина",
            "genre": "гаївка (веснянка)",
            "region": "Галичина",
            "narrator": "Параска Дідик",
            "year": 1916,
            "content": "Хоровий весняний варіант гри у «ворота», адаптований після перших виступів Українських Січових Стрільців",
            "tags": ["гаївка", "весна", "ворота", "січовики"],
            "verified": True
        }
    ]

    # 1. Зберегти у файл
    filepath = os.path.join(LESSON_DIR, "folklore_archive.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    # 2. Прочитати назад
    with open(filepath, "r", encoding="utf-8") as file:
        loaded_records = json.load(file)

    print(f"Завантажено {len(loaded_records)} записів")

    # 3. Вивести заголовки
    print("\n=== Архів експедиції ===")
    for i, record in enumerate(loaded_records, 1):
        print(
            f"{i}. \"{record['title']}\" ({record['genre']}, {record['region']})")


# Завдання 3: Клас FolkloreRecord
class FolkloreRecord:
    """Клас для однієї фольклорної записі"""

    def __init__(self, title: str, genre: str, region: str, narrator: str,
                 year: int, content: str, tags: List[str], verified: bool):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self) -> Dict:
        """Повертає словник із усіма атрибутами"""
        return {
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Класовий метод: створює об'єкт зі словника"""
        return cls(
            data["title"],
            data["genre"],
            data["region"],
            data["narrator"],
            data["year"],
            data["content"],
            data["tags"],
            data["verified"]
        )

    def __str__(self) -> str:
        """Красивий вивод запису"""
        verified_status = "(перевірено)" if self.verified else "(не перевірено)"
        return f"[{self.genre}] \"{self.title}\" — {self.region}, {self.year} {verified_status} (оповідач: {self.narrator})"


# Завдання 4: Клас FieldExpedition
class FieldExpedition:
    """Клас польової експедиції збирача фольклору"""

    def __init__(self, expedition_id: int, researcher: str, location: str, date: str):
        self.expedition_id = expedition_id
        self.researcher = researcher
        self.location = location
        self.date = date
        self.records: List[FolkloreRecord] = []

    def add_record(self, record: FolkloreRecord) -> str:
        """Додає запис до експедиції"""
        for existing_record in self.records:
            if existing_record.title == record.title:
                return f"Запис '{record.title}' вже є в експедиції"

        self.records.append(record)
        return f"Запис '{record.title}' додано до експедиції"

    def remove_record(self, title: str) -> str:
        """Видаляє запис за назвою"""
        for i, record in enumerate(self.records):
            if record.title == title:
                removed = self.records.pop(i)
                return f"Запис '{title}' видалено"

        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre: str) -> List[FolkloreRecord]:
        """Повертає список записів заданого жанру"""
        return [record for record in self.records if record.genre == genre]

    def to_dict(self) -> Dict:
        """Повертає словник для JSON"""
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": [record.to_dict() for record in self.records]
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Класовий метод: відновлює об'єкт з JSON"""
        expedition = cls(
            data["expedition_id"],
            data["researcher"],
            data["location"],
            data["date"]
        )
        expedition.records = [FolkloreRecord.from_dict(
            record_data) for record_data in data["records"]]
        return expedition

    def save(self, filepath: str) -> None:
        """Зберігає експедицію у JSON-файл"""
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=2, ensure_ascii=False)

    def load(self, filepath: str) -> None:
        """Завантажує експедицію з файлу"""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            restored = self.from_dict(data)
            self.expedition_id = restored.expedition_id
            self.researcher = restored.researcher
            self.location = restored.location
            self.date = restored.date
            self.records = restored.records
        except FileNotFoundError:
            print(f"Файл {filepath} не знайдено")
        except json.JSONDecodeError:
            print(f"Помилка при розборі JSON з файлу {filepath}")

# Завдання 5: Центральний архів


def merge_archives(filepaths: List[str]) -> List[FolkloreRecord]:
    """Об'єднує експедиції з кількох файлів"""
    all_records = []

    for filepath in filepaths:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

                # Перевіряємо, чи це експедиція чи просто список записів
                if isinstance(data, dict) and "records" in data:
                    # Це експедиція - беремо записи з поля "records"
                    for record_data in data["records"]:
                        record = FolkloreRecord.from_dict(record_data)
                        all_records.append(record)
                elif isinstance(data, list):
                    # Це просто список записів
                    for record_data in data:
                        record = FolkloreRecord.from_dict(record_data)
                        all_records.append(record)
                else:
                    print(
                        f"Попередження: файл {filepath} має невідомий формат")

        except FileNotFoundError:
            print(f"Попередження: файл {filepath} не знайдено, пропускаємо")
        except json.JSONDecodeError:
            print(f"Попередження: файл {filepath} пошкоджено, пропускаємо")

    return all_records


def filter_records(records: List[FolkloreRecord], genre: Optional[str] = None,
                   region: Optional[str] = None, verified: Optional[bool] = None) -> List[FolkloreRecord]:
    """Фільтрує записи за критеріями"""
    filtered = records

    if genre is not None:
        filtered = [r for r in filtered if r.genre == genre]

    if region is not None:
        filtered = [r for r in filtered if r.region == region]

    if verified is not None:
        filtered = [r for r in filtered if r.verified == verified]

    return filtered


def export_summary(records: List[FolkloreRecord], filepath: str) -> None:
    """Експортує зведення в JSON-файл"""
    summary_data = []

    for record in records:
        summary_data.append({
            "title": record.title,
            "genre": record.genre,
            "region": record.region,
            "verified": record.verified
        })

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(summary_data, file, indent=2, ensure_ascii=False)

    print(f"Зведення експортовано в {filepath}")


# Бонус: функція find_duplicates
def find_duplicates(filepaths: List[str]) -> Dict[str, List[str]]:
    """Знаходить дублікати записів по назві"""
    all_records = []

    for filepath in filepaths:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

                # Перевіряємо формат файлу
                if isinstance(data, dict) and "records" in data:
                    for record_data in data["records"]:
                        all_records.append(
                            FolkloreRecord.from_dict(record_data))
                elif isinstance(data, list):
                    for record_data in data:
                        all_records.append(
                            FolkloreRecord.from_dict(record_data))

        except FileNotFoundError:
            print(f"Попередження: файл {filepath} не знайдено, пропускаємо")
        except json.JSONDecodeError:
            print(f"Попередження: файл {filepath} пошкоджено, пропускаємо")

    duplicates = {}

    for record in all_records:
        if record.title not in duplicates:
            duplicates[record.title] = []

        for other_record in all_records:
            if record.title == other_record.title and other_record.region != record.region:
                if other_record.region not in duplicates[record.title]:
                    duplicates[record.title].append(other_record.region)

    return duplicates


# Демонстрація всіх завдань
if __name__ == "__main__":
    print("=== Домашнє завдання: Робота з JSON ===\n")

    # Завдання 1: Серіалізація вручну
    print("=== Завдання 1: Серіалізація вручну ===")
    task1_serialization()

    print("\n")

    # Завдання 2: Архів експедиції
    print("=== Завдання 2: Архів експедиції ===")
    task2_archive()

    print("\n")

    # Завдання 3: Клас FolkloreRecord
    print("=== Завдання 3: Клас FolkloreRecord ===")

    # Створення об'єктів
    record1 = FolkloreRecord(
        "Ой у лузі червона калина", "пісня", "Полтавщина",
        "Ганна Остапенко", 1932,
        "Красива дівчина з червоним вінком",
        ["калина", "вінок", "дівчина"], True
    )

    record2 = FolkloreRecord(
        "Ой у лузі червона калина похилилася", "козацька балада", "Харківщина",
        "Мокрина Куличка", 1885,
        "Давній козацький варіант (основа «Розлилися круті бережечки»), записаний експедицією Миколи Лисенка",
        ["козаки", "калина", "журба"], True
    )

    record3 = FolkloreRecord(
        "Ой у лузі червона калина похилилася", "стрілецька пісня", "Волинь",
        "Настя Селегейна", 1943,
        "Повстанський варіант з доповненими куплетами про батька, що ховав сина-стрільця",
        ["стрільці", "війна", "батько", "син"], True
    )

    print(record1)
    print(record2)
    print(record3)

    # Перевірка повного циклу
    print("\n=== Перевірка повного циклу ===")

    # Збереження
    records_list = [record1, record2, record3]
    filepath = os.path.join(LESSON_DIR, "records.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump([r.to_dict() for r in records_list],
                  file, indent=2, ensure_ascii=False)

    # Завантаження
    with open(filepath, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        restored_records = [FolkloreRecord.from_dict(
            data) for data in loaded_data]

    for record in restored_records:
        print(record)

    print("\n")

    # Завдання 4: Клас FieldExpedition
    print("=== Завдання 4: Клас FieldExpedition ===")

    expedition = FieldExpedition(
        1, "Дмитро Яворницький", "Карпати", "2026-09-04")

    print(expedition.add_record(record1))
    print(expedition.add_record(record2))
    print(expedition.add_record(record2))  # дублікат

    print(expedition.find_by_genre("пісня"))
    print(expedition.find_by_genre("казка"))

    expedition.remove_record("Про лисицю та журавля")
    print(expedition.remove_record("Невідома"))  # не існує

    expedition_filepath = os.path.join(LESSON_DIR, "expedition.json")
    expedition.save(expedition_filepath)
    print("Експедиція збережена")

    # Завантаження
    expedition.load(expedition_filepath)
    print("Експедиція завантажена")

    print("\n")

    # Завдання 5: Центральний архів
    print("=== Завдання 5: Центральний архів ===")

    # Створення тестових файлів
    expedition1 = FieldExpedition(
        1, "Дмитро Яворницький", "Карпати", "2026-09-04")
    expedition1.add_record(record1)
    expedition1.add_record(record2)

    expedition2 = FieldExpedition(
        2, "Філарет Колесса", "Полтавщина", "2026-09-05")
    expedition2.add_record(record3)

    # Додамо ту саму пісню з іншого регіону для демонстрації дублікатів
    record_duplicate = FolkloreRecord(
        "Ой у лузі червона калина", "пісня", "Харківщина",
        "Іван Петренко", 1945,
        "Інший варіант пісні з Харківщини",
        ["калина", "вінок", "пісня"], True
    )
    expedition2.add_record(record_duplicate)

    expedition1_path = os.path.join(LESSON_DIR, "expedition1.json")
    expedition2_path = os.path.join(LESSON_DIR, "expedition2.json")

    expedition1.save(expedition1_path)
    expedition2.save(expedition2_path)

    # Об'єднання
    merged = merge_archives([expedition1_path, expedition2_path])
    print(f"Об'єднано {len(merged)} записів")

    # Фільтрація
    kyiv_records = filter_records(merged, region="Полтавщина")
    print(f"Записів з Полтавщини: {len(kyiv_records)}")

    # Зведення
    summary_path = os.path.join(LESSON_DIR, "summary.json")
    export_summary(merged, summary_path)

    print("\n")

    # Бонус: find_duplicates
    print("=== Бонус: Пошук дублікатів ===")
    duplicates = find_duplicates([expedition1_path, expedition2_path])

    for title, regions in duplicates.items():
        print(f"{title}: {', '.join(regions)}")

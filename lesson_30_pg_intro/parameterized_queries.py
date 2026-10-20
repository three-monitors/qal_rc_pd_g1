import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
DSN = os.getenv("DATABASE_URL")


def demonstrate_sql_injection():
    """Показати різницю між небезпечним та безпечним кодом"""

    print("=== ПАРАМЕТРИЗОВАНІ ЗАПИТИ ===\n")

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            # Тестові дані
            print("1️⃣  Вставляємо тестові дані:\n")

            cur.execute(
                "INSERT INTO clients (name, phone, email) VALUES (%s, %s, %s);",
                ("Олена Коваленко", "+380-67-123-45-67", "olena@example.com")
            )
            conn.commit()
            print("✅ Вставлено: Олена Коваленко\n")

            # Безпечний пошук (параметризований запит)
            print("2️⃣  БЕЗПЕЧНИЙ пошук за іменем:\n")
            search_name = "Олена Коваленко"

            cur.execute(
                "SELECT id, name, phone, email FROM clients WHERE name = %s;",
                (search_name,)
            )
            result = cur.fetchone()
            if result:
                print(f"✅ Знайдено: {result}\n")

            # Небезпечна спроба (мовна ілюстрація — НЕ виконуємо!)
            print("3️⃣  НЕБЕЗПЕЧНИЙ код (для демонстрації):\n")
            print("❌ НІКОЛИ не робіть так:")
            dangerous_name = "admin'; DROP TABLE clients; --"
            dangerous_query = f"SELECT * FROM clients WHERE name = '{dangerous_name}';"
            print(f"   {dangerous_query}")
            print("   ^ Це видалить всю таблицю клієнтів!\n")

            # Правильний спосіб з параметрами
            print("4️⃣  ПРАВИЛЬНИЙ спосіб (параметризований запит):\n")
            print("✅ Завжди використовуйте параметри (%s)!")
            print(
                "   cur.execute(\"SELECT * FROM clients WHERE name = %s;\", (search_name,))")
            print("   ^ Це захищає від SQL-ін'єкцій!\n")


if __name__ == "__main__":
    demonstrate_sql_injection()

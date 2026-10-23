from database import engine, Base, init_db
from sqlalchemy import text
from models import *  # Імпортувати всі моделі

if __name__ == "__main__":
    print("🔄 Створення схеми lesson36...")
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS lesson36"))
        conn.commit()

    print("🔄 Ініціалізація БД...")
    init_db()
    print("✅ Таблиці успішно створені!")

    # Перевірити таблиці
    print("\n📊 Створені таблиці:")
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")

import os
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Шукаємо .env в батьківській директорії
load_dotenv(Path(__file__).parent.parent.parent / '.env')

# Конфігурація
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не знайдено в .env файлі")

# Створити Engine
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Встановити True для дебагу
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True  # Перевіряти з'єднання перед використанням
)

# Declarative Base
Base = declarative_base()

# SessionLocal для створення сесій
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Функція для отримання сесії (для dependency injection)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Функція для ініціалізації БД
def init_db():
    """Створити всі таблиці"""
    Base.metadata.create_all(bind=engine)
    print("✅ БД ініціалізована")

# Функція для очистки БД (для тестування)
def drop_db():
    """Видалити всі таблиці"""
    Base.metadata.drop_all(bind=engine)
    print("✅ БД очищена")


# Перевірка підключення
if __name__ == "__main__":
    print("🔄 Перевірка підключення до БД...")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Підключення успішне!")
            print(f"📊 PostgreSQL версія: {version[:50]}...")
    except Exception as e:
        print(f"❌ Помилка підключення: {e}")

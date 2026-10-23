from database import engine, Base, drop_db
from models import *

if __name__ == "__main__":
    print("🧹 Очищення БД від таблиць уроку 36...")
    drop_db()
    print("✅ Таблиці видалені!")

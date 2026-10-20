import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
DSN = os.getenv("DATABASE_URL")


def create_tables():
    """Створити таблиці для Service Management System"""

    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:

                # Клієнти
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS clients (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(150) NOT NULL,
                        phone VARCHAR(20),
                        email VARCHAR(100),
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                """)
                print("✅ Таблиця clients створена")

                # Послуги
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS services (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(150) NOT NULL,
                        description TEXT,
                        price DECIMAL(10, 2) NOT NULL,
                        duration_minutes INTEGER,
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                """)
                print("✅ Таблиця services створена")

                # Замовлення / Записи
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS orders (
                        id SERIAL PRIMARY KEY,
                        client_id INTEGER NOT NULL,
                        service_id INTEGER NOT NULL,
                        order_date DATE NOT NULL,
                        status VARCHAR(50) DEFAULT 'created',
                        total_price DECIMAL(10, 2) NOT NULL,
                        notes TEXT,
                        created_at TIMESTAMP DEFAULT NOW(),
                        FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
                        FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE RESTRICT
                    );
                """)
                print("✅ Таблиця orders створена")

                # Інвентар (запчастини / матеріали)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS inventory (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(150) NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit_price DECIMAL(10, 2),
                        min_quantity INTEGER DEFAULT 0,
                        created_at TIMESTAMP DEFAULT NOW()
                    );
                """)
                print("✅ Таблиця inventory створена")

                conn.commit()
                print("\n✅ Всі таблиці створені: clients, services, orders, inventory")

                # Вивести інформацію про створені таблиці
                cur.execute("""
                    SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public';
                """)
                tables = cur.fetchall()
                print(f"\n📊 Таблиці в БД: {', '.join([t[0] for t in tables])}")

    except psycopg.Error as e:
        print(f"❌ Помилка: {e}")


if __name__ == "__main__":
    create_tables()

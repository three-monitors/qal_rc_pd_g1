import os
from dotenv import load_dotenv
import psycopg
from dataclasses import dataclass
from typing import Optional, List

load_dotenv()
DSN = os.getenv("DATABASE_URL")


@dataclass
class Client:
    id: int
    name: str
    phone: str
    email: str


class ClientRepository:
    """Репозиторій для роботи з клієнтами"""

    def __init__(self, dsn: str):
        self.dsn = dsn

    def create(self, name: str, phone: str, email: str) -> int:
        """Створити клієнта, повернути ID"""
        with psycopg.connect(self.dsn) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "INSERT INTO clients (name, phone, email) VALUES (%s, %s, %s) RETURNING id;",
                        (name, phone, email)
                    )
                    client_id = cur.fetchone()[0]
                    conn.commit()
                    return client_id
                except psycopg.IntegrityError as e:
                    print(f"❌ Помилка: {e}")
                    return None

    def read(self, client_id: int) -> Optional[Client]:
        """Отримати клієнта по ID"""
        with psycopg.connect(self.dsn) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, phone, email FROM clients WHERE id = %s;",
                    (client_id,)
                )
                row = cur.fetchone()
                if row:
                    return Client(*row)
                return None

    def read_all(self) -> List[Client]:
        """Отримати всіх клієнтів"""
        with psycopg.connect(self.dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone, email FROM clients;")
                return [Client(*row) for row in cur.fetchall()]

    def update(self, client_id: int, name: str = None, phone: str = None, email: str = None) -> bool:
        """Оновити клієнта"""
        with psycopg.connect(self.dsn) as conn:
            with conn.cursor() as cur:
                if name and phone and email:
                    cur.execute(
                        "UPDATE clients SET name = %s, phone = %s, email = %s WHERE id = %s;",
                        (name, phone, email, client_id)
                    )
                elif name:
                    cur.execute(
                        "UPDATE clients SET name = %s WHERE id = %s;",
                        (name, client_id)
                    )
                elif phone:
                    cur.execute(
                        "UPDATE clients SET phone = %s WHERE id = %s;",
                        (phone, client_id)
                    )
                elif email:
                    cur.execute(
                        "UPDATE clients SET email = %s WHERE id = %s;",
                        (email, client_id)
                    )
                else:
                    return False

                conn.commit()
                return cur.rowcount > 0

    def delete(self, client_id: int) -> bool:
        """Видалити клієнта"""
        with psycopg.connect(self.dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM clients WHERE id = %s;", (client_id,))
                conn.commit()
                return cur.rowcount > 0


# Тестування CRUD операцій
if __name__ == "__main__":
    repo = ClientRepository(DSN)

    print("=== CRUD ОПЕРАЦІЇ ДЛЯ КЛІЄНТІВ ===\n")

    # CREATE
    print("📝 CREATE — додавання клієнтів:")
    client_id_1 = repo.create(
        "Олена Коваленко", "+380-67-123-45-67", "olena@example.com")
    client_id_2 = repo.create(
        "Іван Петренко", "+380-50-987-65-43", "ivan@example.com")
    print(f"✅ Клієнти створені: ID {client_id_1}, {client_id_2}\n")

    # READ ONE
    print("📖 READ — отримання клієнта:")
    client = repo.read(client_id_1)
    if client:
        print(f"✅ {client.name}: {client.phone}\n")

    # READ ALL
    print("📚 READ ALL — отримання всіх клієнтів:")
    clients = repo.read_all()
    for c in clients:
        print(f"  - {c.name} ({c.phone})")
    print()

    # UPDATE
    print("✏️  UPDATE — оновлення клієнта:")
    success = repo.update(client_id_1, email="newemail@example.com")
    if success:
        print(f"✅ Клієнт оновлений\n")

    # DELETE
    print("🗑️  DELETE — видалення клієнта:")
    success = repo.delete(client_id_2)
    if success:
        print(f"✅ Клієнт видалений\n")

    # Фінальна перевірка
    print("📊 Фінальний список клієнтів:")
    clients = repo.read_all()
    for c in clients:
        print(f"  - {c.name} ({c.phone})")

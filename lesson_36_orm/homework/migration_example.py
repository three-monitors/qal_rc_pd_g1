"""
Порівняння: "сирий" SQL vs SQLAlchemy ORM
"""

import os
import inspect
from database import SessionLocal, engine
import psycopg
from models import Client, Service, Order

# ❌ СТАРИЙ СПОСІБ — "сирий" SQL через psycopg
def old_add_client_sql(name: str, phone: str, email: str):
    """SQL версія"""
    conn = psycopg.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO lesson36.clients (name, phone, email) VALUES (%s, %s, %s)",
            (name, phone, email)
        )
        conn.commit()
        print(f"✅ SQL: клієнт {name} доданий")
    finally:
        cur.close()
        conn.close()


def old_get_clients_sql():
    """SQL версія"""
    conn = psycopg.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    try:
        cur.execute("SELECT id, name, phone FROM lesson36.clients")
        rows = cur.fetchall()
        clients = [{"id": row[0], "name": row[1], "phone": row[2]}
                   for row in rows]
        return clients
    finally:
        cur.close()
        conn.close()


def old_update_client_sql(client_id: int, email: str):
    """SQL версія"""
    conn = psycopg.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    try:
        cur.execute(
            "UPDATE lesson36.clients SET email = %s WHERE id = %s",
            (email, client_id)
        )
        conn.commit()
        print(f"✅ SQL: клієнт {client_id} оновлений")
    finally:
        cur.close()
        conn.close()


def old_get_client_orders_sql(client_id: int):
    """SQL версія з JOIN"""
    conn = psycopg.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT c.name, o.id, o.status
            FROM lesson36.clients c
            LEFT JOIN lesson36.orders o ON c.id = o.client_id
            WHERE c.id = %s
        """, (client_id,))

        rows = cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()

# ✅ НОВИЙ СПОСІБ — SQLAlchemy ORM
def new_add_client_orm(name: str, phone: str, email: str):
    """ORM версія"""
    session = SessionLocal()
    try:
        client = Client(name=name, phone=phone, email=email)
        session.add(client)
        session.commit()
        print(f"✅ ORM: клієнт {name} доданий")
    finally:
        session.close()


def new_get_clients_orm():
    """ORM версія"""
    session = SessionLocal()
    try:
        clients = session.query(Client).all()
        return [{"id": c.id, "name": c.name, "phone": c.phone} for c in clients]
    finally:
        session.close()


def new_update_client_orm(client_id: int, email: str):
    """ORM версія"""
    session = SessionLocal()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            client.email = email
            session.commit()
            print(f"✅ ORM: клієнт {client_id} оновлений")
    finally:
        session.close()


def new_get_client_orders_orm(client_id: int):
    """ORM версія (автоматично через relationship)"""
    session = SessionLocal()
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            # Прямий доступ до замовлень через relationship!
            return [(client.name, order.id, order.status) for order in client.orders]
        return []
    finally:
        session.close()


# ===== ПОРІВНЯННЯ =====
if __name__ == "__main__":
    print("=== ПОРІВНЯННЯ: SQL vs ORM ===\n")

    # ADD
    print("1. ADD CLIENT")
    sql_lines = len(inspect.getsource(old_add_client_sql).split('\n'))
    orm_lines = len(inspect.getsource(new_add_client_orm).split('\n'))
    print(f"   SQL: {sql_lines} рядків")
    print(f"   ORM: {orm_lines} рядків")
    print(f"   Економія: {round((1 - orm_lines / sql_lines) * 100)}% коду!\n")

    # GET
    print("2. GET CLIENTS")
    sql_lines = len(inspect.getsource(old_get_clients_sql).split('\n'))
    orm_lines = len(inspect.getsource(new_get_clients_orm).split('\n'))
    print(f"   SQL: {sql_lines} рядків (з управлінням з'єднанням)")
    print(f"   ORM: {orm_lines} рядків")
    print(f"   Економія: {round((1 - orm_lines / sql_lines) * 100)}% коду!\n")

    # UPDATE
    print("3. UPDATE CLIENT")
    sql_lines = len(inspect.getsource(old_update_client_sql).split('\n'))
    orm_lines = len(inspect.getsource(new_update_client_orm).split('\n'))
    print(f"   SQL: {sql_lines} рядків")
    print(f"   ORM: {orm_lines} рядків")
    print(f"   Економія: {round((1 - orm_lines / sql_lines) * 100)}% коду!\n")

    # JOIN
    print("4. GET CLIENT WITH ORDERS (JOIN)")
    sql_lines = len(inspect.getsource(old_get_client_orders_sql).split('\n'))
    orm_lines = len(inspect.getsource(new_get_client_orders_orm).split('\n'))
    print(f"   SQL: {sql_lines} рядків (вручну писати JOIN)")
    print(f"   ORM: {orm_lines} рядків (автоматичне завантаження!)")
    print(f"   Економія: {round((1 - orm_lines / sql_lines) * 100)}% коду!\n")

    # Загальна економія
    total_sql = (len(inspect.getsource(old_add_client_sql).split('\n')) +
                 len(inspect.getsource(old_get_clients_sql).split('\n')) +
                 len(inspect.getsource(old_update_client_sql).split('\n')) +
                 len(inspect.getsource(old_get_client_orders_sql).split('\n')))

    total_orm = (len(inspect.getsource(new_add_client_orm).split('\n')) +
                 len(inspect.getsource(new_get_clients_orm).split('\n')) +
                 len(inspect.getsource(new_update_client_orm).split('\n')) +
                 len(inspect.getsource(new_get_client_orders_orm).split('\n')))

    total_savings = round((1 - total_orm / total_sql) * 100)

    print(f"📊 ЗАГАЛЬНА СТАТИСТИКА:")
    print(f"   Всього SQL коду: {total_sql} рядків")
    print(f"   Всього ORM коду: {total_orm} рядків")
    print(f"   Загальна економія: {total_savings}% коду!")
    print(f"\n✨ Висновок: ORM дозволяє писати на {total_savings}% менше коду!")
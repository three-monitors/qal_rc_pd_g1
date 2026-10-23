from database import SessionLocal
from models import Client, Service, Order
from crud_operations import ClientCRUD, ServiceCRUD, OrderCRUD


def test_client_crud():
    """Тестування Client CRUD"""
    print("=== TEST CLIENT CRUD ===\n")

    session = SessionLocal()

    # CREATE
    print("1️⃣ CREATE — додавання клієнта")
    client = ClientCRUD.create(
        session, "Олена Петренко", "+380501234567", "olena@example.com")
    print(f"✅ Клієнт створений: ID {client.id}, {client.name}\n")

    # READ
    print("2️⃣ READ — отримання клієнта")
    fetched = ClientCRUD.get_by_phone(session, "+380501234567")
    print(f"✅ Знайдено: {fetched.name} ({fetched.phone})\n")

    # UPDATE
    print("3️⃣ UPDATE — оновлення клієнта")
    updated = ClientCRUD.update(
        session, client.id, email="olena.new@example.com")
    print(f"✅ Email оновлений: {updated.email}\n")

    # DELETE
    print("4️⃣ DELETE — видалення клієнта")
    deleted = ClientCRUD.delete(session, client.id)
    print(f"✅ Клієнт видалений: {deleted}\n")

    session.close()


def test_service_crud():
    """Тестування Service CRUD"""
    print("=== TEST SERVICE CRUD ===\n")

    session = SessionLocal()

    # CREATE
    print("1️⃣ CREATE — додавання послуги")
    service = ServiceCRUD.create(
        session, "Манікюр", 300.00, 60, "Класичний манікюр")
    print(f"✅ Послуга створена: ID {service.id}, {service.name}\n")

    # READ
    print("2️⃣ READ — отримання послуги")
    fetched = ServiceCRUD.get_by_id(session, service.id)
    print(f"✅ Знайдено: {fetched.name} ({fetched.price} грн)\n")

    # UPDATE
    print("3️⃣ UPDATE — оновлення ціни")
    updated = ServiceCRUD.update(session, service.id, price=350.00)
    print(f"✅ Ціна оновлена: {updated.price}\n")

    # DELETE
    print("4️⃣ DELETE — видалення послуги")
    deleted = ServiceCRUD.delete(session, service.id)
    print(f"✅ Послуга видалена: {deleted}\n")

    session.close()


def test_order_crud():
    """Тестування Order CRUD"""
    print("=== TEST ORDER CRUD ===\n")

    session = SessionLocal()

    # Створити клієнта для тесту
    client = ClientCRUD.create(session, "Тест Клієнт", "+380509876543")

    # CREATE
    print("1️⃣ CREATE — додавання замовлення")
    order = OrderCRUD.create(session, client.id, "scheduled")
    print(f"✅ Замовлення створено: ID {order.id}\n")

    # READ
    print("2️⃣ READ — отримання замовлення")
    fetched = OrderCRUD.get_by_id(session, order.id)
    print(f"✅ Знайдено: ID {fetched.id}, статус {fetched.status}\n")

    # UPDATE
    print("3️⃣ UPDATE — оновлення статусу")
    updated = OrderCRUD.update(session, order.id, status="in_progress")
    print(f"✅ Статус оновлений: {updated.status}\n")

    # Очистка
    OrderCRUD.delete(session, order.id)
    ClientCRUD.delete(session, client.id)

    session.close()


if __name__ == "__main__":
    test_client_crud()
    test_service_crud()
    test_order_crud()
    print("\n✅ Все тести пройшли успішно!")

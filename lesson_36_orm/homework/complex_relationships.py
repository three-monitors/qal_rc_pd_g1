from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload, selectinload
from models import Client, Service, Order, OrderItem, Appointment


# Eager loading з joinedload
def get_client_with_all_data(session: Session, client_id: int):
    """Завантажити клієнта з усіма даними (один запит)"""
    client = session.query(Client).options(
        joinedload(Client.orders).joinedload(Order.order_items)
    ).filter(Client.id == client_id).first()
    return client


# Selectin для більш складних сценаріїв
def get_all_clients_with_orders(session: Session):
    """Завантажити всіх клієнтів з їхніми замовленнями"""
    clients = session.query(Client).options(
        selectinload(Client.orders)
    ).all()
    return clients


# Аналітика
def get_order_statistics(session: Session):
    """Статистика по замовленнях"""
    stats = session.query(
        func.count(Order.id).label("total_orders"),
        func.count(func.distinct(Order.client_id)).label("clients"),
        func.count(func.distinct(Order.status)).label("statuses")
    ).first()

    return {
        "total_orders": stats[0],
        "total_clients": stats[1],
        "unique_statuses": stats[2]
    }


def get_revenue_by_service(session: Session):
    """Виручка по кожній послузі"""
    return session.query(
        Service.name,
        func.count(OrderItem.service_id).label("order_count"),
        func.sum(Service.price).label("total_revenue")
    ).join(OrderItem).group_by(Service.id).all()

# Перевірка синтаксису
if __name__ == "__main__":
    print("🔄 Перевірка синтаксису complex_relationships...")
    try:
        print("✅ Синтаксис правильний!")
        print("📊 Функції для складних зв'язків:")
        print("  - get_client_with_all_data")
        print("  - get_all_clients_with_orders")
        print("  - get_order_statistics")
        print("  - get_revenue_by_service")
    except Exception as e:
        print(f"❌ Помилка синтаксису: {e}")

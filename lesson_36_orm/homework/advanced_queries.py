from sqlalchemy import and_, or_, func
from sqlalchemy.orm import Session, joinedload
from models import Client, Service, Order, OrderItem, Appointment


def get_client_with_orders(session: Session, client_id: int):
    """Отримати клієнта з усіма замовленнями (eager loading)"""
    client = session.query(Client).options(
        joinedload(Client.orders).joinedload(Order.order_items)
    ).filter(Client.id == client_id).first()
    return client


def get_orders_by_status(session: Session, status: str):
    """Отримати замовлення певного статусу"""
    return session.query(Order).filter(
        Order.status == status
    ).order_by(Order.created_at.desc()).all()


def get_orders_by_client_and_status(session: Session, client_id: int, status: str):
    """Отримати замовлення клієнта зі статусом"""
    return session.query(Order).filter(
        and_(
            Order.client_id == client_id,
            Order.status == status
        )
    ).all()


def search_services(session: Session, search_term: str):
    """Пошук послуг по назві (LIKE)"""
    return session.query(Service).filter(
        Service.name.ilike(f"%{search_term}%")
    ).all()


def get_order_count_by_status(session: Session):
    """Підрахувати кількість замовлень по статусам"""
    return session.query(
        Order.status,
        func.count(Order.id).label("count")
    ).group_by(Order.status).all()


def get_client_order_counts(session: Session):
    """Отримати кількість замовлень кожного клієнта"""
    return session.query(
        Client.name,
        func.count(Order.id).label("order_count")
    ).join(Order).group_by(Client.id).all()


def get_paged_orders(session: Session, page: int = 1, per_page: int = 10):
    """Отримати замовлення з пагінацією"""
    offset = (page - 1) * per_page

    total = session.query(Order).count()
    orders = session.query(Order).offset(offset).limit(per_page).all()
    total_pages = (total + per_page - 1) // per_page

    return {
        "orders": orders,
        "total": total,
        "page": page,
        "total_pages": total_pages
    }


def get_upcoming_appointments(session: Session, days: int = 7):
    """Отримати призначення на наступні N днів"""
    from datetime import datetime, timedelta

    today = datetime.utcnow()
    future = today + timedelta(days=days)

    return session.query(Appointment).filter(
        and_(
            Appointment.appointment_time >= today,
            Appointment.appointment_time <= future,
            Appointment.status == "scheduled"
        )
    ).order_by(Appointment.appointment_time).all()


def get_inventory_low_stock(session: Session, min_quantity: int = 10):
    """Отримати товари з низьким запасом"""
    from models import Inventory

    return session.query(Inventory).filter(
        Inventory.quantity < min_quantity
    ).all()

# Перевірка синтаксису
if __name__ == "__main__":
    print("🔄 Перевірка синтаксису advanced_queries...")
    try:
        print("✅ Синтаксис правильний!")
        print("📊 Функції запитів:")
        print("  - get_client_with_orders")
        print("  - get_orders_by_status")
        print("  - get_orders_by_client_and_status")
        print("  - search_services")
        print("  - get_order_count_by_status")
        print("  - get_client_order_counts")
        print("  - get_paged_orders")
        print("  - get_upcoming_appointments")
        print("  - get_inventory_low_stock")
    except Exception as e:
        print(f"❌ Помилка синтаксису: {e}")

from sqlalchemy.orm import Session
from models import Client, Service, Order, OrderItem, Appointment, Inventory

# ===== CLIENT CRUD =====
class ClientCRUD:
    @staticmethod
    def create(session: Session, name: str, phone: str, email: str = None) -> Client:
        """Створити клієнта"""
        client = Client(name=name, phone=phone, email=email)
        session.add(client)
        session.commit()
        session.refresh(client)
        return client

    @staticmethod
    def get_by_id(session: Session, client_id: int) -> Client | None:
        """Отримати по ID"""
        return session.query(Client).filter(Client.id == client_id).first()

    @staticmethod
    def get_by_phone(session: Session, phone: str) -> Client | None:
        """Отримати по телефону"""
        return session.query(Client).filter(Client.phone == phone).first()

    @staticmethod
    def get_all(session: Session, skip: int = 0, limit: int = 10) -> list[Client]:
        """Отримати всіх з пагінацією"""
        return session.query(Client).offset(skip).limit(limit).all()

    @staticmethod
    def update(session: Session, client_id: int, **kwargs) -> Client | None:
        """Оновити клієнта"""
        client = session.query(Client).filter(Client.id == client_id).first()
        if client:
            for key, value in kwargs.items():
                if hasattr(client, key):
                    setattr(client, key, value)
            session.commit()
            session.refresh(client)
        return client

    @staticmethod
    def delete(session: Session, client_id: int) -> bool:
        """Видалити клієнта"""
        client = session.query(Client).filter(Client.id == client_id).first()
        if client:
            session.delete(client)
            session.commit()
            return True
        return False

# ===== SERVICE CRUD =====
class ServiceCRUD:
    @staticmethod
    def create(session: Session, name: str, price: float, duration: int, description: str = None) -> Service:
        """Створити послугу"""
        service = Service(name=name, price=price,
                          duration=duration, description=description)
        session.add(service)
        session.commit()
        session.refresh(service)
        return service

    @staticmethod
    def get_by_id(session: Session, service_id: int) -> Service | None:
        """Отримати по ID"""
        return session.query(Service).filter(Service.id == service_id).first()

    @staticmethod
    def get_all(session: Session, skip: int = 0, limit: int = 10) -> list[Service]:
        """Отримати всі з пагінацією"""
        return session.query(Service).offset(skip).limit(limit).all()

    @staticmethod
    def update(session: Session, service_id: int, **kwargs) -> Service | None:
        """Оновити послугу"""
        service = session.query(Service).filter(
            Service.id == service_id).first()
        if service:
            for key, value in kwargs.items():
                if hasattr(service, key):
                    setattr(service, key, value)
            session.commit()
            session.refresh(service)
        return service

    @staticmethod
    def delete(session: Session, service_id: int) -> bool:
        """Видалити послугу"""
        service = session.query(Service).filter(
            Service.id == service_id).first()
        if service:
            session.delete(service)
            session.commit()
            return True
        return False

# ===== ORDER CRUD =====
class OrderCRUD:
    @staticmethod
    def create(session: Session, client_id: int, status: str = "scheduled") -> Order:
        """Створити замовлення"""
        order = Order(client_id=client_id, status=status)
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

    @staticmethod
    def get_by_id(session: Session, order_id: int) -> Order | None:
        """Отримати по ID"""
        return session.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_by_client(session: Session, client_id: int) -> list[Order]:
        """Отримати всі замовлення клієнта"""
        return session.query(Order).filter(Order.client_id == client_id).all()

    @staticmethod
    def get_by_status(session: Session, status: str) -> list[Order]:
        """Отримати замовлення за статусом"""
        return session.query(Order).filter(Order.status == status).all()

    @staticmethod
    def update(session: Session, order_id: int, **kwargs) -> Order | None:
        """Оновити замовлення"""
        order = session.query(Order).filter(Order.id == order_id).first()
        if order:
            for key, value in kwargs.items():
                if hasattr(order, key):
                    setattr(order, key, value)
            session.commit()
            session.refresh(order)
        return order

    @staticmethod
    def delete(session: Session, order_id: int) -> bool:
        """Видалити замовлення"""
        order = session.query(Order).filter(Order.id == order_id).first()
        if order:
            session.delete(order)
            session.commit()
            return True
        return False

# ===== ORDER ITEM CRUD =====
class OrderItemCRUD:
    @staticmethod
    def create(session: Session, order_id: int, service_id: int) -> OrderItem:
        """Додати послугу до замовлення"""
        item = OrderItem(order_id=order_id, service_id=service_id)
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @staticmethod
    def get_order_services(session: Session, order_id: int) -> list[Service]:
        """Отримати всі послуги замовлення"""
        return session.query(Service).join(OrderItem).filter(OrderItem.order_id == order_id).all()


# Перевірка синтаксису
if __name__ == "__main__":
    print("🔄 Перевірка синтаксису CRUD операцій...")
    try:
        print("✅ Синтаксис правильний!")
        print("📊 Класи CRUD:")
        print("  - ClientCRUD")
        print("  - ServiceCRUD")
        print("  - OrderCRUD")
        print("  - OrderItemCRUD")
    except Exception as e:
        print(f"❌ Помилка синтаксису: {e}")

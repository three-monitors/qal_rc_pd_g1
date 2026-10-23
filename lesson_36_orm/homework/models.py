from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Text, Boolean, Numeric
from sqlalchemy.orm import relationship
from database import Base
import enum


class OrderStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class AppointmentStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = {'schema': 'lesson36'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.now())

    # Relationships
    orders = relationship("Order", back_populates="client",
                          cascade="all, delete-orphan")
    appointments = relationship(
        "Appointment", back_populates="client", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', phone='{self.phone}')>"


class Service(Base):
    __tablename__ = "services"
    __table_args__ = {'schema': 'lesson36'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    duration = Column(Integer, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now())

    # Relationships
    order_items = relationship(
        "OrderItem", back_populates="service", cascade="all, delete-orphan")
    appointments = relationship(
        "Appointment", back_populates="service", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Service(id={self.id}, name='{self.name}', price={self.price})>"


class Order(Base):
    __tablename__ = "orders"
    __table_args__ = {'schema': 'lesson36'}

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey(
        "lesson36.clients.id"), nullable=False)
    status = Column(Enum(OrderStatus), nullable=False,
                    default=OrderStatus.SCHEDULED)
    created_at = Column(DateTime, default=datetime.now())

    # Relationships
    client = relationship("Client", back_populates="orders")
    order_items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, client_id={self.client_id}, status={self.status})>"


class OrderItem(Base):
    __tablename__ = "order_items"
    __table_args__ = {'schema': 'lesson36'}

    order_id = Column(Integer, ForeignKey(
        "lesson36.orders.id"), primary_key=True)
    service_id = Column(Integer, ForeignKey(
        "lesson36.services.id"), primary_key=True)

    # Relationships
    order = relationship("Order", back_populates="order_items")
    service = relationship("Service", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, service_id={self.service_id})>"


class Appointment(Base):
    __tablename__ = "appointments"
    __table_args__ = {'schema': 'lesson36'}

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey(
        "lesson36.clients.id"), nullable=False)
    service_id = Column(Integer, ForeignKey(
        "lesson36.services.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(Enum(AppointmentStatus), nullable=False,
                    default=AppointmentStatus.SCHEDULED)
    created_at = Column(DateTime, default=datetime.now())

    # Relationships
    client = relationship("Client", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, client_id={self.client_id}, time={self.appointment_time})>"


class Inventory(Base):
    __tablename__ = "inventory"
    __table_args__ = {'schema': 'lesson36'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"<Inventory(id={self.id}, name='{self.name}', quantity={self.quantity})>"


# Перевірка синтаксису
if __name__ == "__main__":
    print("🔄 Перевірка синтаксису моделей...")
    try:
        from database import Base
        print(f"✅ Синтаксис правильний!")
        print(f"📊 Знайдено моделей: {len(Base.metadata.tables)}")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
    except Exception as e:
        print(f"❌ Помилка синтаксису: {e}")

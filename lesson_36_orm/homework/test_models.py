import pytest
from database import SessionLocal
from models import Client, Service, Order
from crud_operations import ClientCRUD, ServiceCRUD, OrderCRUD


@pytest.fixture
def session():
    """Fixture для сесії (використовує ту саму БД для тестування)"""
    session = SessionLocal()
    yield session
    session.close()


class TestClientCRUD:
    def test_create_client(self, session):
        client = ClientCRUD.create(
            session, "Test Client", "+380501234567", "test@example.com")
        assert client.id is not None
        assert client.name == "Test Client"
        # Очистка
        ClientCRUD.delete(session, client.id)

    def test_get_client_by_phone(self, session):
        created = ClientCRUD.create(
            session, "Alice", "+380509876543", "alice@example.com")
        fetched = ClientCRUD.get_by_phone(session, "+380509876543")
        assert fetched.id == created.id
        # Очистка
        ClientCRUD.delete(session, created.id)

    def test_update_client(self, session):
        client = ClientCRUD.create(
            session, "Bob", "+380501112223", "bob@example.com")
        updated = ClientCRUD.update(
            session, client.id, email="bob.new@example.com")
        assert updated.email == "bob.new@example.com"
        # Очистка
        ClientCRUD.delete(session, client.id)

    def test_delete_client(self, session):
        client = ClientCRUD.create(
            session, "Charlie", "+380503334445", "charlie@example.com")
        deleted = ClientCRUD.delete(session, client.id)
        assert deleted == True
        fetched = ClientCRUD.get_by_id(session, client.id)
        assert fetched is None


class TestServiceCRUD:
    def test_create_service(self, session):
        service = ServiceCRUD.create(session, "Test Service", 100.00, 30)
        assert service.id is not None
        assert service.name == "Test Service"
        # Очистка
        ServiceCRUD.delete(session, service.id)

    def test_get_service_by_id(self, session):
        created = ServiceCRUD.create(session, "Service A", 200.00, 60)
        fetched = ServiceCRUD.get_by_id(session, created.id)
        assert fetched.id == created.id
        # Очистка
        ServiceCRUD.delete(session, created.id)

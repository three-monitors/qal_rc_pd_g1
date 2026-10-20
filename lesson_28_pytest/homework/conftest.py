from source import BankAccount
import pytest
import logging
import sys
import os

# Додаємо батьківську директорію в PYTHONPATH
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


# Налаштування логування
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('example.log', encoding="utf8")
    ]
)


@pytest.fixture
def zero_account():
    """Фікстура для нульового рахунку з teardown"""
    acc = BankAccount(0)
    yield acc
    del acc


@pytest.fixture
def one_000_account():
    """Фікстура для рахунку 1000 з teardown"""
    acc = BankAccount(1000)
    yield acc
    del acc

import pytest
from source import BankAccount
import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "initial_balance",
    [0, 100, 1000],
    ids=["zero_balance", "100_balance", "1000_balance"]
)
def test_initial_balance(initial_balance):
    """Тест початкового балансу"""
    # Arrange
    expected_balance = initial_balance

    # Act
    account = BankAccount(initial_balance)

    # Assert
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "init_balance, amount",
    [
        (0, 1),
        (100, 1),
        (1000, 100),
    ],
    ids=[
        "zero_plus_one",
        "100_plus_one",
        "1000_plus_100",
    ]
)
def test_deposit(init_balance, amount):
    """Тест поповнення рахунку з параметризацією"""
    # Arrange
    account = BankAccount(init_balance)
    expected_balance = init_balance + amount

    # Act
    account.deposit(amount)

    logger.debug(
        "Initial=%s amount=%s actual=%s expected=%s",
        init_balance,
        amount,
        account.balance,
        expected_balance,
    )

    # Assert
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "amount",
    [-1, -0.01, -100],
    ids=[
        "negative_one",
        "negative_fraction",
        "negative_hundred",
    ]
)
def test_negative_deposit(zero_account, amount):
    """Тест негативного поповнення з параметризацією"""
    # Arrange
    expected_error = ValueError
    expected_message = "For deposit amount should be large than zero"

    logger.debug(
        "Testing negative deposit: amount=%s expected_error=%s",
        amount,
        expected_error.__name__
    )

    # Act & Assert
    with pytest.raises(expected_error, match=expected_message):
        zero_account.deposit(amount)


def test_zero_account_without_changes(zero_account):
    """Тест нульового рахунку без змін"""
    # Arrange
    expected_balance = 0

    # Act
    actual_balance = zero_account.balance

    # Assert
    assert actual_balance == expected_balance


def test_1000_account_without_changes(one_000_account):
    """Тест рахунку 1000 без змін"""
    # Arrange
    expected_balance = 1000

    # Act
    actual_balance = one_000_account.balance

    # Assert
    assert actual_balance == expected_balance

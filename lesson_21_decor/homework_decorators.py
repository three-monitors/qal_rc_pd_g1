import logging
import functools
import time
from typing import Callable, Optional
import random

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s"
)


# Завдання 1: Козацька хроніка
def chronicle(scribe_name: Optional[str] = None):
    """
    Декоратор для логування викликів функції: назва, аргументи, результат.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            scribe = scribe_name or "Анонімний"

            # Форматування аргументів
            if args:
                args_str = ", ".join(repr(arg) for arg in args)
            else:
                args_str = ""

            logging.info(f"[Літописець: {scribe}] Викликано: {func.__name__}({args_str})")
            
            result = func(*args, **kwargs)
            
            logging.info(f"[Результат]: {result}")
            return result
        return wrapper
    return decorator


# Завдання 2: Хранитель фортеці
def guard(secret: str):
    """
    Декоратор для перевірки пароля перед викликом функції.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            password = input("Назви пароль: ")
            
            if password == secret:
                logging.info(f"Доступ надано: {func.__name__}")
                return func(*args, **kwargs)
            else:
                logging.warning(f"Невдала спроба доступу до: {func.__name__}")
                print("Стій! Доступ заборонено.")
                return None
        return wrapper
    return decorator


# Завдання 3: Залізний характер
def retry(times: int = 3, delay: float = 1.0):
    """
    Декоратор для повторних спроб при помилках.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                    logging.info(f"Успіх на спробі {attempt}/{times}")
                    return result
                except Exception as e:
                    if attempt == times:
                        logging.error(f"Всі спроби вичерпано")
                        return None
                    else:
                        logging.warning(f"Спроба {attempt}/{times} не вдалася: {e}")
                        time.sleep(delay)
        return wrapper
    return decorator


def main():
    """Демонстрація всіх декораторів"""
    print("=== Завдання 1: Козацька хроніка ===")
    
    @chronicle("Самійло Величко")
    def make_decision(action, target):
        return f"Рішення: {action} → {target}"
    
    @chronicle()
    def count_warriors(regiment):
        return 500
    
    make_decision("Атакувати", "Перекоп")
    count_warriors("Полтавський")
    
    print("\n=== Завдання 2: Хранитель фортеці ===")
    
    @guard(secret="Мамай")
    def open_treasury():
        print("Скарбниця відчинена!")
        return "золото, срібло, зброя"
    
    result = open_treasury()
    # print(f"Результат: {result}")

    print("\n=== Завдання 3: Залізний характер ===")

    @retry(times=4, delay=0.5)
    def unreliable_scout():
        if random.random() < 0.7:  # 70% шанс провалу
            raise ConnectionError("Розвідник не повернувся")
        return "Ворог за річкою!"

    result = unreliable_scout()
    # print(f"Результат: {result}")


if __name__ == "__main__":
    main()

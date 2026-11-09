from pathlib import Path
from typing import Callable, Tuple


# Завдання 1: Фабрика перетворювачів напруги
def make_voltage_converter(factor: float) -> Callable[[float], float]:
    """Повертає функцію-перетворювач напруги"""
    def converter(voltage: float) -> float:
        return voltage * factor
    return converter


# Завдання 2: Лічильник електроенергії
def make_electricity_meter(address: str, initial_kwh: float = 0.0) -> Tuple[Callable, Callable, Callable]:
    """Повертає три функції для керування лічильником"""
    current_kwh = initial_kwh

    def add(kwh: float) -> float:
        nonlocal current_kwh
        current_kwh += kwh
        return current_kwh

    def reset() -> float:
        nonlocal current_kwh
        current_kwh = initial_kwh
        return current_kwh

    def report() -> str:
        return f"Адреса: {address} | Спожито: {current_kwh} кВт·год"

    return add, reset, report


# Завдання 3: Диспетчер аварійних подій
def make_dispatcher(station_name: str) -> Callable:
    """Повертає функцію диспетчера"""
    def dispatch(event: str, callback: Callable[[str], None]) -> None:
        message = f"# [{station_name}] {event}"
        callback(message)
    return dispatch


def log_to_console(message: str) -> None:
    """Виводить повідомлення в консоль"""
    print(message)


def log_to_file(message: str) -> None:
    """Записує повідомлення у файл"""
    from pathlib import Path
    # Визначаємо папку поточного файлу
    current_dir = Path(__file__).parent
    log_file = current_dir / "dispatch_log.txt"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")


# Завдання 4: Сортування підстанцій
def make_sorter(field: str, reverse: bool = False) -> Callable:
    """Повертає функцію сортування"""
    def sorter(items):
        return sorted(items, key=lambda x: x[field], reverse=reverse)
    return sorter


# Бонус: Захисний автомат (circuit breaker)
def make_circuit_breaker(max_failures: int) -> Callable:
    """Повертає функцію-обгортку для захисту"""
    failure_count = 0

    def protect(func):
        def wrapper(*args, **kwargs):
            nonlocal failure_count
            if failure_count >= max_failures:
                raise RuntimeError("Автомат вимкнено!")

            try:
                return func(*args, **kwargs)
            except Exception:
                failure_count += 1
                raise

        return wrapper

    return protect


def main():
    """Демонстрація всіх завдань"""
    print("=== Завдання 1: Фабрика перетворювачів напруги ===")
    step_up = make_voltage_converter(10.0)   # підвищувальний
    step_down = make_voltage_converter(0.5)  # знижувальний

    print("step_up = make_voltage_converter(10.0)  # підвищувальний")
    print("step_down = make_voltage_converter(0.5)  # знижувальний\n")
    print(f"step_up(22.0) = {step_up(22.0)}")      # 220.0
    print(f"step_down(220.0) = {step_down(220.0)}")  # 110.0
    print(f"step_up(11.0) = {step_up(11.0)}")      # 110.0

    print("\n=== Завдання 2: Лічильник електроенергії ===")
    add, reset, report = make_electricity_meter("вул. Франка, 12", 150.0)

    print('add, reset, report = make_electricity_meter("вул. Франка, 12", 150.0)\n')
    print(f"print(add(30.5)) = {add(30.5)}")    # 180.5
    print(f"print(add(14.0)) = {add(14.0)}")    # 194.5
    # Адреса: вул. Франка, 12 | Спожито: 194.5 кВт·год
    print(f"print(report()) = {report()}")
    print(f"print(reset()) = {reset()}")        # 150.0
    # Адреса: вул. Франка, 12 | Спожито: 150.0 кВт·год
    print(f"print(report()) = {report()}")

    print("\n=== Завдання 3: Диспетчер аварійних подій ===")
    dispatch = make_dispatcher("Підстанція №7 Івано-Франківськ")

    print('dispatch = make_dispatcher("Підстанція №7 Івано-Франківськ")')
    print('\ndispatch("Перевищення напруги", log_to_console)')
    dispatch("Перевищення напруги", log_to_console)
    print('\ndispatch("Коротке замикання", log_to_console')
    dispatch("Коротке замикання", log_to_console)
    print('\ndispatch("Відновлення живлення", log_to_file)')
    dispatch("Відновлення живлення", log_to_file)

    print("\n=== Завдання 4: Сортування підстанцій ===")
    substations = [
        {"name": "Підстанція №3", "region": "Коломия",        "load_kw": 4500},
        {"name": "Підстанція №7", "region": "Івано-Франківськ", "load_kw": 8200},
        {"name": "Підстанція №1", "region": "Калуш",           "load_kw": 3100},
        {"name": "Підстанція №9", "region": "Надвірна",        "load_kw": 6700},
    ]

    sort_by_load = make_sorter("load_kw", reverse=True)
    print("\nСортування за навантаженням:\n")
    for s in sort_by_load(substations):
        print(f"#  {s['name']} {s['load_kw']}")

    sort_by_name = make_sorter("name")
    print("\nСортування за назвою:\n")
    for s in sort_by_name(substations):
        print(f"#  {s['name']}")

    print("\n=== Бонус: Захисний автомат (circuit breaker) ===")
    breaker = make_circuit_breaker(max_failures=2)

    def unstable_sensor():
        raise ConnectionError("Сенсор не відповідає")

    safe_sensor = breaker(unstable_sensor)

    try:
        safe_sensor()  # ConnectionError: Сенсор не відповідає (помилка 1)
    except ConnectionError as e:
        print(f"safe_sensor() # ConnectionError: {e} (помилка 1)")

    try:
        safe_sensor()  # ConnectionError: Сенсор не відповідає (помилка 2)
    except ConnectionError as e:
        print(f"safe_sensor() # ConnectionError: {e} (помилка 2)")

    try:
        safe_sensor()  # RuntimeError: Автомат вимкнено! (автомат спрацював)
    except RuntimeError as e:
        print(f"safe_sensor() # RuntimeError: {e} (автомат спрацював)")

    try:
        safe_sensor()  # RuntimeError: Автомат вимкнено! (автомат спрацював)
    except RuntimeError as e:
        print(f"safe_sensor() # RuntimeError: {e} (автомат спрацював)")


if __name__ == "__main__":
    main()

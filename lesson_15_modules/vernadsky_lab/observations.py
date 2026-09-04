from datetime import date
from vernadsky_lab.minerals import get_mineral

_journal = []


def record(researcher, mineral_name, note):
    """Записує спостереження в журнал"""
    mineral = get_mineral(mineral_name)

    if mineral is None:
        return f"Мінерал '{mineral_name}' не зареєстровано. Спочатку додайте його до каталогу"

    entry = {
        "researcher": researcher,
        "mineral": mineral_name,
        "note": note,
        "date": date.today()
    }
    _journal.append(entry)
    return f"Спостереження записано: {researcher} → {mineral_name}"


def get_observations(mineral_name=None):
    """Повертає записи про конкретний мінерал або всі записи"""
    if mineral_name:
        return [entry for entry in _journal if entry["mineral"] == mineral_name]
    return _journal.copy()

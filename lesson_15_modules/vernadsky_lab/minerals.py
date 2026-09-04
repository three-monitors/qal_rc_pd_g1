from datetime import date

MINERAL_CATALOG = {
    "Апатит": {
        "formula": "Ca₅(PO₄)₃(F,Cl,OH)",
        "hardness": 5,
        "origin": "Карелия",
        "discovered": 1830
    },
    "Топаз": {
        "formula": "Al₂SiO₄(F,OH)₂",
        "hardness": 8,
        "origin": "Бразилія",
        "discovered": 1800
    },
    "Гранат": {
        "formula": "X₃Y₂(SiO₄)₃",
        "hardness": 7,
        "origin": "Кавказ",
        "discovered": 1790
    },
    "Польовий_шпат": {
        "formula": "KAlSi₃O₈",
        "hardness": 6,
        "origin": "Україна",
        "discovered": 1700
    },
    "Слюда": {
        "formula": "KAl₂(AlSi₃O₁₀)(F,OH)₂",
        "hardness": 3,
        "origin": "Карпати",
        "discovered": 1650
    }
}


def get_mineral(name):
    """Повертає словник із даними про мінерал"""
    return MINERAL_CATALOG.get(name)


def register_mineral(name, formula, hardness, origin, discovered):
    """Додає новий мінерал до каталогу"""
    if name in MINERAL_CATALOG:
        return f"Мінерал '{name}' вже зареєстровано в каталозі"

    if not 1 <= hardness <= 10:
        return "Некоректна твердість: має бути від 1 до 10"

    MINERAL_CATALOG[name] = {
        "formula": formula,
        "hardness": hardness,
        "origin": origin,
        "discovered": discovered
    }
    return f"Мінерал '{name}' додано до каталогу"

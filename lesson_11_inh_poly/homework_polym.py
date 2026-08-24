class Cossack:
    def __init__(self, name, kurin, weapons=None):
        """Конструктор класу Cossack"""
        self.name = name  # ім'я
        self.kurin = kurin  # курінь
        self.weapons = weapons if weapons else []  # зброя
        self.victories = 0  # кількість перемог
        self.rank = "козак"  # звання

    def update_rank(self):
        """Оновлює звання залежно від кількості перемог"""
        if self.victories >= 7:
            self.rank = "полковник"
        elif self.victories >= 3:
            self.rank = "осавул"
        else:
            self.rank = "козак"

    def arm(self, weapon):
        """Додає зброю до арсеналу козака"""
        if weapon in self.weapons:
            # "<ім'я> вже має <зброя>!"
            return f"{self.name} вже має {weapon}!"

        self.weapons.append(weapon)
        return f"{self.name} озброєний {weapon}!"

    # перемога в бою (ворог)
    def win_battle(self, enemy):
        """Збільшує лічильник перемог"""
        self.victories += 1
        self.update_rank()
        # "<ім'я> переміг <ворог>! Слава козаку!"
        return f"{self.name} переміг {enemy}! Слава козаку!"

    def __str__(self):
        """Красивий вивід об'єкта"""
        weapons_str = ", ".join(
            self.weapons) if self.weapons else "немає зброї"
        # Козак <ім'я> | Курінь: <курінь> | Звання: <rank>} | Перемоги: <victories> | Зброя: <зброя через кому>
        return f"Козак {self.name} | Курінь: {self.kurin} | Звання: {self.rank} | Перемоги: {self.victories} | Зброя: {weapons_str}"


class ZaporozhianSich:
    def __init__(self, name, capacity):
        """Конструктор класу ZaporozhianSich"""
        self.name = name  # назва
        self.cossacks = []  # список козаків
        self.capacity = capacity  # максимальна кількість козаків

    def enlist(self, cossack):
        """Приймає об'єкт класу Cossack і додає його до Січі"""
        if len(self.cossacks) >= self.capacity:
            return "Січ переповнена!"  # "Січ переповнена!"

        for existing_cossack in self.cossacks:
            if existing_cossack.name == cossack.name:
                return f"{cossack.name} вже на Січі!"  # "<ім'я> вже на Січі!"

        self.cossacks.append(cossack)
        return f"{cossack.name} зарахований на Січ!"

    def dismiss(self, name):
        """Видаляє козака за іменем"""
        for i, cossack in enumerate(self.cossacks):
            if cossack.name == name:
                dismissed = self.cossacks.pop(i)
                return f"Козак {name} покинув Січ!"

        return f"Козака {name} не знайдено!"  # "Козака <ім'я> не знайдено!"

    def call_to_battle(self, enemy):
        """Викликає козаків на бій"""
        if len(self.cossacks) == 0:
            return "Нікому боронити Січ!"  # "Нікому боронити Січ!"

        # "Військо Запорозьке виступає проти <ворог>! У поході <кількість> козаків!"
        return f"Військо Запорозьке виступає проти {enemy}! У поході {len(self.cossacks)} козаків!"

    def best_warrior(self):
        """Повертає козака з найбільшою кількістю перемог"""
        if len(self.cossacks) == 0:
            return "Січ порожня!"  # "Січ порожня!"

        best_cossack = self.cossacks[0]
        for cossack in self.cossacks:
            if cossack.victories > best_cossack.victories:
                best_cossack = cossack

        return f"Найкращий воїн: {best_cossack.name} ({best_cossack.victories} перемог)"

    def roster(self):
        """Повертає список імен усіх козаків"""
        if len(self.cossacks) == 0:
            return "На Січі нікого немає"  # "На Січі нікого немає"

        names = [cossack.name for cossack in self.cossacks]
        return ", ".join(names)

    def promote_all(self):
        """Оновлює звання всіх козаків"""
        for cossack in self.cossacks:
            cossack.update_rank()
        return "Звання всіх козаків оновлено!"


# Приклад очікуваної роботи
if __name__ == "__main__":
    # Завдання 1
    print("=== Завдання 1 ===")
    cossack = Cossack("Іван Сірко", "Кальміуський")
    print(cossack.arm("шабля"))
    # Іван Сірко озброєний шабля!
    print(cossack.arm("мушкет"))
    # Іван Сірко озброєний мушкет!
    print(cossack.win_battle("яничари"))
    # Іван Сірко переміг яничари! Слава козаку! / print не перемога
    print(cossack)
    # Козак Іван Сірко | Курінь: Кальміуський | Звання: козак | Перемоги: 1 | Зброя: шабля, мушкет

    print("\n")

    # Завдання 2
    print("=== Завдання 2 ===")
    sich = ZaporozhianSich("Чортомлицька Січ", capacity=3)

    # новий об'єкт
    ivan = Cossack("Іван Сірко", "Кальміуський")
    petro = Cossack("Петро Сагайдачний", "Канівський")

    ivan.win_battle("яничари")  # перемога Івана Сірко 1
    ivan.win_battle("татари")  # перемога Івана Сірко 2
    petro.win_battle("поляки")  # перемога Петра Сагайдачного 1

    sich.enlist(ivan)
    sich.enlist(petro)

    print(sich.call_to_battle("турки"))
    # Військо Запорозьке виступає проти турки! У поході 2 козаків!
    print(sich.best_warrior())
    # Найкращий воїн: Іван Сірко (2 перемог)
    print(sich.roster())
    # Іван Сірко, Петро Сагайдачний

    print("\n")

    # Бонус
    print("=== Бонус ===")
    ivan.victories = 0          # 0 перемог
    print(f"До перемог: {ivan.rank}")  # До перемог: козак / 0 перемог
    ivan.win_battle("ногайці")  # 1 перемога
    ivan.win_battle("ногайці")  # 2 перемога
    ivan.win_battle("ногайці")  # 3 перемога
    print(f"Після {ivan.victories} перемог: {ivan.rank}")  # Після 3 перемог: осавул
    ivan.win_battle("ногайці")  # 4 перемога
    ivan.win_battle("ногайці")  # 5 перемога
    ivan.win_battle("ногайці")  # 6 перемога
    ivan.win_battle("ногайці")  # 7 перемога
    print(f"Після {ivan.victories} перемог: {ivan.rank}")  # Після 7 перемог: полковник
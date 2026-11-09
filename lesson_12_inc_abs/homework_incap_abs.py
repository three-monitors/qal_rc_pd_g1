from abc import ABC, abstractmethod

# Завдання 1
class MagicCreature(ABC):
    """Абстрактний клас для казкових істот зі східнослов'янської міфології"""

    def __init__(self, name, magic_level, health):
        """Конструктор класу MagicCreature"""
        self.name = name  # ім'я
        self._magic_level = self._validate_magic_level(
            magic_level)  # рівень магії / захищений
        self.__health = self._validate_health(health)  # здоров'я / приватний
        self.__alive = True if self.__health > 0 else False  # чи жива істота / приватний

    def _validate_magic_level(self, level):
        """Приватний метод валідації рівня магії"""
        if not 1 <= level <= 10:
            raise ValueError("Рівень магії має бути від 1 до 10!")
        return level

    def _validate_health(self, health):
        """Приватний метод валідації здоров'я"""
        if not 0 <= health <= 100:
            raise ValueError("Здоров'я має бути від 0 до 100!")
        return health

    @property
    def health(self):
        """Геттер для здоров'я"""
        return self.__health

    @health.setter
    def health(self, value):
        """Сеттер для здоров'я з перевіркою на смерть"""
        self.__health = self._validate_health(value)
        if self.__health <= 0:  # якщо здоров'я стає 0 або менше
            self.__health = 0  # встановлює 0
            self.__alive = False  # позначає істоту як мертву

    @property
    def magic_level(self):
        """Геттер для рівня магії"""
        return self._magic_level  # повертає рівень магії

    @magic_level.setter
    def magic_level(self, value):
        """Сеттер для рівня магії"""
        self._magic_level = self._validate_magic_level(
            value)  # перевіряє діапазон

    @property
    def is_alive(self):
        """Геттер для статусу живий/мертвий"""
        return self.__alive  # повертає `True` або `False`

    @abstractmethod
    def use_ability(self):
        """Абстрактний метод - кожна істота має свою здібність"""
        pass

    @abstractmethod
    def describe(self):
        """Абстрактний метод - кожна істота описує себе по-своєму"""
        pass

    @abstractmethod  # бонус
    def weakness(self):
        """Абстрактний метод - кожна істота має свою слабкість"""
        pass

    def take_damage(self, amount):
        """Зменшує здоров'я на amount"""
        if not self.__alive:
            return f"{self.name} вже переміг смерть... або ні."

        self.health = self.health - amount
        return f"{self.name} отримав {amount} пошкоджень!"

    def __str__(self):
        """Красивий вивід об'єкта"""
        return f"{self.name} | Магія: {self._magic_level} | HP: {self.__health} | Живий: {self.__alive}"

# Завдання 2
class Molfar(MagicCreature):
    """Мольфар — карпатський чаклун, який керує силами природи"""

    def __init__(self, name, magic_level, health, element, spells):
        """Конструктор класу Molfar"""
        super().__init__(name, magic_level, health)
        self.element = element  # стихія
        self.__spells = spells  # запас заклинань

    @property
    def spells(self):
        """Геттер для заклинань"""
        return self.__spells

    @spells.setter
    def spells(self, value):
        """Сеттер для заклинань - тільки невід'ємні значення"""
        if value < 0:
            raise ValueError("Кількість заклинань не може бути від'ємною!")
        self.__spells = value

    def use_ability(self):
        """Використовує заклинання стихії"""
        if self.__spells > 0:
            self.__spells = self.__spells - 1
            return f"Мольфар {self.name} закликає {self.element}! Залишилось заклинань: {self.__spells}"
        else:
            return f"Мольфар {self.name} виснажений - сила стихій покинула його!"

    def describe(self):
        """Описує мольфара"""
        return f"Мольфар {self.name}, повелитель стихії {self.element}. Рівень магії: {self.magic_level}"

    def weakness(self):  # бонус
        """Слабкість мольфара"""
        return "протилежна стихія"


class Rusalka(MagicCreature):
    """Русалка — небезпечна водяна істота, що принаджує мандрівників"""

    def __init__(self, name, magic_level, health, river, charm_power):
        """Конструктор класу Rusalka"""
        super().__init__(name, magic_level, health)
        self.river = river  # річка де мешкає
        self.__charm_power = charm_power  # сила чар

    @property
    def charm_power(self):
        """Геттер для сили чар"""
        return self.__charm_power

    @charm_power.setter
    def charm_power(self, value):
        """Сеттер для сили чар - діапазон 1-5"""
        if not 1 <= value <= 5:
            raise ValueError("Сила чар має бути від 1 до 5!")
        self.__charm_power = value

    def use_ability(self):
        """Зачаровує мандрівника"""
        result = f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.__charm_power}"
        if self.__charm_power == 5:
            result += " Ніхто не встоїть!"
        return result

    def describe(self):
        """Описує русалку"""
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.__charm_power}/5"

    def weakness(self):  # бонус
        """Слабкість русалки"""
        return "сонячне світло"


class Perelesnyk(MagicCreature):
    """Перелесник — вогняний дух, що літає між світами"""

    def __init__(self, name, magic_level, health, speed, form):
        """Конструктор класу Perelesnyk"""
        super().__init__(name, magic_level, health)
        self.__speed = speed  # швидкість польоту
        self.form = form  # форма

    @property
    def speed(self):
        """Геттер для швидкості"""
        return self.__speed

    @speed.setter
    def speed(self, value):
        """Сеттер для швидкості - діапазон 1-100"""
        if not 1 <= value <= 100:
            raise ValueError("Швидкість має бути від 1 до 100!")
        self.__speed = value

    def change_form(self):
        """Перемикає між формами"""
        if self.form == "вогняна куля":
            self.form = "людська"
        else:
            self.form = "вогняна куля"
        return f"Перелесник перетворився на {self.form}!"

    def use_ability(self):
        """Мчить крізь ніч"""
        result = f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.__speed}! Форма: {self.form}"
        if self.form == "людська":
            result += " Ніхто не здогадається..."
        return result

    def describe(self):
        """Описує перелесника"""
        return f"Перелесник {self.name}. Швидкість: {self.__speed}. Зараз у формі: {self.form}"

    def weakness(self):  # бонус
        """Слабкість перелесника"""
        return "священна вода"

# Завдання 3
class EnchantedForest:
    """Зачарований ліс, де мешкають казкові істоти"""

    def __init__(self, name, capacity):
        """Конструктор класу EnchantedForest"""
        self.name = name  # назва лісу
        self.__creatures = []  # приватний список істот
        self.capacity = capacity  # максимальна кількість мешканців

    def add_creature(self, creature):
        """Додає істоту до лісу"""
        if len(self.__creatures) >= self.capacity:
            return f"Зачарований ліс {self.name} переповнений!"

        if not creature.is_alive:
            return "Мертві істоти не можуть оселитись у лісі!"

        for existing_creature in self.__creatures:
            if existing_creature.name == creature.name:
                return f"{creature.name} вже мешкає у цьому лісі!"

        self.__creatures.append(creature)
        return f"{creature.name} оселився у {self.name}!"

    def remove_creature(self, name):
        """Видаляє істоту за іменем"""
        for i, creature in enumerate(self.__creatures):
            if creature.name == name:
                removed = self.__creatures.pop(i)
                return f"{name} покинув {self.name}!"

        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self):
        """Повертає істоту з найвищим рівнем магії"""
        if len(self.__creatures) == 0:
            return "Ліс порожній - нема кому чаклувати!"

        powerful = self.__creatures[0]
        for creature in self.__creatures:
            if creature.magic_level > powerful.magic_level:
                powerful = creature

        return f"Найпотужніша істота: {powerful.name} (рівень магії: {powerful.magic_level})"

    def attack_intruder(self, intruder_name):
        """Кожна жива істота атакує вторгнення"""
        if len(self.__creatures) == 0:
            return f"Ліс беззахисний перед {intruder_name}!"

        results = []
        for creature in self.__creatures:
            if creature.is_alive:
                ability = creature.use_ability()
                weakness = creature.weakness()
                # бонус / слабкість кожної істоти разом із її здібністю
                results.append(f"{ability} Слабкість: {weakness}")

        return results

    def census(self):
        """Повертає опис усіх живих істот"""
        alive_creatures = [
            creature for creature in self.__creatures
            if creature.is_alive
        ]

        if len(alive_creatures) == 0:
            return ["Ліс порожній"]

        descriptions = [creature.describe() for creature in alive_creatures]
        return descriptions

    @property
    def creatures_count(self):
        """Геттер для кількості живих істот у лісі"""
        count = 0
        for creature in self.__creatures:
            if creature.is_alive:
                count += 1
        return count

    def heal_all(self, amount):  # бонус
        """Відновлює здоров'я всіх живих істот на amount (але не більше 100)"""
        for creature in self.__creatures:
            if creature.is_alive:
                new_health = creature.health + amount
                if new_health > 100:
                    new_health = 100
                creature.health = new_health
        return f"Усі живі істоти вилікувано на {amount} здоров'я!"


# Приклад очікуваної роботи
if __name__ == "__main__":
    # Зачарований ліс, де мешкають усі казкові істоти
    forest = EnchantedForest("Чорний Ліс", capacity=5)

    # Створення істот
    molfar = Molfar("Юрій", magic_level=8, health=90,
                    element="вогонь", spells=3)
    rusalka = Rusalka("Калина", magic_level=6, health=100,
                      river="Дніпро", charm_power=5)
    perelesnyk = Perelesnyk("Іскра", magic_level=7,
                            health=85, speed=95, form="вогняна куля")

    # Додавання істот до лісу
    print(forest.add_creature(molfar))
    print(forest.add_creature(rusalka))
    print(forest.add_creature(perelesnyk))

    print("\n")

    # Перевірка найпотужнішої істоти
    print(forest.most_powerful())

    print("\n")

    # Атака на вторгнення
    print("=== Атака на мисливця ===")
    attack_results = forest.attack_intruder("мисливець")
    for result in attack_results:
        print(result)

    print("\n")

    # Перелесник змінює форму
    print(perelesnyk.change_form())
    print(perelesnyk.use_ability())

    print("\n")

    # Мольфар отримує пошкодження
    print(molfar.take_damage(90))
    print(f"Мольфар живий: {molfar.is_alive}")
    print(molfar)

    print("\n")

    # Перепис лісу
    print("=== Перепис лісу ===")
    census = forest.census()
    for description in census:
        print(description)

    print("\n")

    # Кількість живих істот
    print(f"Кількість живих істот: {forest.creatures_count}")

    print("\n")

    # Лікування всіх істот
    print(forest.heal_all(50))
    print(f"Мольфар здоров'я після лікування: {molfar.health}")
    print(f"Мольфар живий: {molfar.is_alive}")

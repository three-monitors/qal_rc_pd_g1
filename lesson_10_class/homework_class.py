class QuestRoom:
    def __init__(self, name, difficulty, player_limit):
        """Конструктор класу QuestRoom"""
        self.name = name
        self.difficulty = difficulty
        self.player_limit = player_limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        """Додає гравця до кімнати"""
        if len(self.players) >= self.player_limit:
            return "No free slots!"

        if name in self.players:
            return "Player already in room!"

        self.players.append(name)
        self.events_log.append(f"Player {name} joined")
        return f"Player {name} added!"

    def start(self):
        """Запускає квест"""
        if len(self.players) == 0:
            return "Room is empty!"

        self.status = "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"

    def __str__(self):
        """Красивий вивод об'єкта"""
        return f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | Players: {len(self.players)}/{self.player_limit}"

    def remove_player(self, name):
        """Видаляє гравця зі списку"""
        if name not in self.players:
            return "Player not found!"

        self.players.remove(name)
        self.events_log.append(f"Player {name} left")
        return f"Player {name} removed!"

    def is_full(self):
        """Перевіряє, чи кімната заповнена"""
        return len(self.players) >= self.player_limit

    def free_slots(self):
        """Повертає кількість вільних місць"""
        return self.player_limit - len(self.players)

    def reset_room(self):
        """Очищає список гравців, ніби почали нову гру"""
        self.status = "finished"
        self.players = []
        self.status = "waiting"
        self.events_log.append("Room reset")
        return "Room reset!"

    def players_list(self):
        """Повертає список імен гравців"""
        if len(self.players) == 0:
            return "No players in the room"
        return self.players

    def show_log(self):
        """Повертає історію всіх подій"""
        return self.events_log


# Прості ручні тести
def run_tests():
    """Прості ручні тести для перевірки роботи класу"""
    print("=== Початок тестування ===\n")

    # Тест 1: Конструктор
    print("Тест 1: Конструктор")
    room = QuestRoom("Піратський острів", 3, 4)
    assert room.name == "Піратський острів"
    assert room.difficulty == 3
    assert room.player_limit == 4
    assert len(room.players) == 0
    assert room.status == "waiting"
    print("✅ Конструктор працює правильно\n")

    # Тест 2: Додавання гравців
    print("Тест 2: Додавання гравців")
    room.add_player("Олег")
    room.add_player("Даша")
    assert len(room.players) == 2
    assert "Олег" in room.players
    assert "Даша" in room.players
    print("✅ Додавання гравців працює правильно\n")

    # Тест 3: Ліміт гравців
    print("Тест 3: Ліміт гравців")
    room.add_player("Анна")
    room.add_player("Петро")
    result = room.add_player("Іван")
    assert result == "No free slots!"
    assert len(room.players) == 4
    print("✅ Ліміт гравців працює правильно\n")

    # Тест 4: Start з гравцями
    print("Тест 4: Start з гравцями")
    result = room.start()
    assert "started with 4 players" in result
    assert room.status == "active"
    print("✅ Start з гравцями працює правильно\n")

    # Тест 5: __str__ метод
    print("Тест 5: __str__ метод")
    str_result = str(room)
    assert "Піратський острів" in str_result
    assert "Difficulty: 3" in str_result
    assert "Players: 4/4" in str_result
    print("✅ __str__ метод працює правильно\n")

    # Тест 6: Видалення гравця
    print("Тест 6: Видалення гравця")
    result = room.remove_player("Олег")
    assert "removed" in result
    assert len(room.players) == 3
    assert "Олег" not in room.players
    print("✅ Видалення гравця працює правильно\n")

    # Тест 7: Видалення неіснуючого гравця
    print("Тест 7: Видалення неіснуючого гравця")
    result = room.remove_player("Неіснуючий")
    assert result == "Player not found!"
    print("✅ Видалення неіснуючого гравця працює правильно\n")

    # Тест 8: is_full
    print("Тест 8: is_full")
    assert room.is_full() == False
    room.add_player("Тимчасовий")
    assert room.is_full() == True
    print("✅ is_full працює правильно\n")

    # Тест 9: free_slots
    print("Тест 9: free_slots")
    room.remove_player("Тимчасовий")
    assert room.free_slots() == 1
    print("✅ free_slots працює правильно\n")

    # Тест 10: reset_room
    print("Тест 10: reset_room")
    result = room.reset_room()
    assert result == "Room reset!"
    assert len(room.players) == 0
    assert room.status == "waiting"
    print("✅ reset_room працює правильно\n")

    # Тест 11: players_list
    print("Тест 11: players_list")
    result = room.players_list()
    assert result == "No players in the room"
    room.add_player("Тестовий")
    result = room.players_list()
    assert "Тестовий" in result
    print("✅ players_list працює правильно\n")

    # Тест 12: show_log
    print("Тест 12: show_log")
    log = room.show_log()
    assert len(log) > 0
    print("✅ show_log працює правильно\n")

    # Тест 13: Start без гравців
    print("Тест 13: Start без гравців")
    room2 = QuestRoom("Тестова кімната", 1, 2)
    result = room2.start()
    assert result == "Room is empty!"
    print("✅ Start без гравців працює правильно\n")

    print("=== Всі тести пройшли успішно! ===")


# Запуск тестів
if __name__ == "__main__":
    print("=== Приклад з завдання 1 ===")
    room = QuestRoom("Піратський острів", 3, 4)
    print(room)
    room.add_player("Олег")
    room.add_player("Даша")
    print(room.start())
    print(room)
    print("\n")

    run_tests()
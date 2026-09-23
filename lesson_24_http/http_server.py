import socket  # Імпорт модуля socket для роботи з мережею

# Створення TCP сокета для HTTP сервера
server = socket.socket(
    socket.AF_INET,  # IPv4 протокол
    socket.SOCK_STREAM,  # TCP надійний протокол (обов'язковий для HTTP)
)

# Прив'язка HTTP сервера до IP та порту
# 127.0.0.1 localhost (адреса сервера)
# 8080 порт для HTTP сервера (80 може бути зайнятий системою)
server.bind(("127.0.0.1", 8080))

# Перехід сокета в режим очікування клієнтів
# Сервер почина чекати HTTP запити від браузерів
server.listen()

print("HTTP Server started on port 8080")

# HTTP відповідь браузеру
# HTTP/1.1 версія протоколу
# 200 OK статус успішного виконання
# <body>...</body> HTML сторінка
response = """
HTTP/1.1 200 OK

<body>
<h1>Hello from Python server</h1>
</body>
"""

# Сервер працює постійно в циклі
while True:
    # Прийом підключення від браузера
    # accept() повертає новий сокет для клієнта та його адресу
    client, address = server.accept()
    print(f"Клієнт підключився: {address}")

    # Отримання HTTP запиту від браузера
    # recv() отримує HTTP запит (максимум 4096 байт)
    request = client.recv(4096)
    print(f"Отримано HTTP запит: {request.decode()}")

    # Надсилання HTTP відповіді браузеру
    # encode() перетворює рядок в байти для передачі по мережі
    client.send(response.encode())

    # Закриття з'єднання з браузером
    client.close()

# Зупинка сервера натиснути Ctrl+C в терміналі
# В браузері відкрийте: http://localhost:8080

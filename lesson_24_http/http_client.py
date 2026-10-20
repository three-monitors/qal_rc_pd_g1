import socket  # Імпорт модуля socket для роботи з мережею

# Створення TCP сокета для HTTP клієнта
client = socket.socket(
    socket.AF_INET,  # IPv4 протокол
    socket.SOCK_STREAM,  # TCP надійний протокол (обов'язковий для HTTP)
)

# Підключення до HTTP сервера
# 127.0.0.1 localhost (адреса сервера)
# 8080 порт HTTP сервера
client.connect(("127.0.0.1", 8080))

# HTTP GET запит
# GET / запит головної сторінки
# HTTP/1.1 версія протоколу
# Host: localhost заголовок з іменем хоста
# \r\n\r\n порожні рядки для завершення HTTP запиту
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"

# Надсилання HTTP запиту серверу
# encode() перетворює рядок в байти для передачі по мережі
client.send(request.encode())

# Отримання HTTP відповіді від сервера
# recv() отримує HTTP відповідь (максимум 4096 байт)
response = client.recv(4096)

# decode() перетворює байти назад в рядок
print(response.decode())

# Закриття з'єднання з сервером
client.close()

# Для перевірки у браузері: http://localhost:8080
# Очікуваний результат: Hello from Python server

# Модулі
from pygame import *
import sys
import socket
import json
from threading import Thread
init()

# Розміри вікна
WIDTH, HEIGHT = 800, 600

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
FPS = 60

# Вікно
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")
clock = time.Clock()

# Підключення до серверу
def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("localhost", 12345))
            id = int(client.recv(24).decode())
            buffer = ""
            game_state = {}

            return id, game_state, buffer, client
        except:
            pass

# Отримання даних
def receive_data():
    global buffer, game_state, game_over
    while not game_over:
        try:
            data = client.recv(2048).decode()
            buffer += data
            while "\n" in buffer:
                packet, buffer = buffer.split('/n', 1)
                if packet.strip():
                    game_state = json.loads(packet)
        except:
            game_state['winner'] = -1

id, game_state, buffer, client = connect_to_server()

# Запуск гри
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.flip()
    clock.tick(FPS)

quit()
sys.exit()
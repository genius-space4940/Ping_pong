# Модулі
import socket
import json
import threading
import time
import random

# Розміри вікна
WIDTH, HEIGHT = 800, 600

# Швидкість м'яча
SPEED_BALL = 4

# Швидкість ракетки
SPEED_PADDLE = 7

# Клас GameServer
class GameServer:
    def __init__(self, host="localhost", port='12345'):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print("Server started...")

        self.clients = {0 : None, 1 : None}
        self.connected = {0 : False, 1 : False}

    def run(self):
        while True:
            self.accept_players()
            self.reset_game_player()
            threading.Thread(target=self.ball, daemon=True).start()

            while not self.game_over and all(self.connected.values()):
                time.sleep(0.1)
            
            print("Гравець переміг")
            time.sleep(5)

            for player_id in [0, 1]:
                try:
                    self.clients[player_id].close()
                except:
                    pass

                self.clients[player_id] = None
                self.connected[player_id] = False

GameServer().run()
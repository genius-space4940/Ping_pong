# Модулі
from pygame import *
import sys
import socket
import json
from threading import Thread
import random
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
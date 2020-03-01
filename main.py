import pygame

from audio_player import AudioPlayer
from threading import Thread
from crank_handler import CrankHandler

audio_player = None
crank_handler = None


def setup():
    global audio_player
    global crank_handler

    audio_player = AudioPlayer()
    audio_player.load_file()
    crank_handler = CrankHandler()


def loop():
    global crank_handler
    while True:
        print(crank_handler.read())


if __name__ == '__main__':
    try:
        setup()
        loop_thread = Thread(target=loop)
        loop_thread.start()
    except KeyboardInterrupt:
        exit()

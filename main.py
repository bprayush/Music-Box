import time

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
    global audio_player
    while True:
        voltage_reading = crank_handler.read()
        print(voltage_reading)

        if voltage_reading > 50:
            audio_player.play()
        else:
            # audio_player.pause()
            pass
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        setup()
        loop_thread = Thread(target=loop)
        loop_thread.start()
    except KeyboardInterrupt:
        exit()

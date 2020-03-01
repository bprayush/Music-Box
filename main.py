import time

from audio_player import AudioPlayer
from threading import Thread
from crank_handler import CrankHandler

audio_player = None
crank_handler = None
timer = 5


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
            if not audio_player.paused:
                timeout()
                audio_player.pause()
        time.sleep(0.1)


def timeout():
    global timer
    time.sleep(timer)


if __name__ == '__main__':
    try:
        setup()
        loop_thread = Thread(target=loop)
        loop_thread.start()
    except KeyboardInterrupt:
        exit()

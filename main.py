#! /usr/bin/python3

import time

from audio_player import AudioPlayer
from threading import Thread
from crank_handler import CrankHandler
import RPi.GPIO as GPIO

audio_player = None
crank_handler = None
timer = 2
button_pin = 18


def setup():
    global audio_player
    global crank_handler
    global button_pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    audio_player = AudioPlayer()
    audio_player.load_file()
    crank_handler = CrankHandler()


def check_button_input():
    global button_pin

    while True:
        if GPIO.input(button_pin):
            print("Button state: ON")


def loop():
    global crank_handler
    global audio_player
    while True:
        voltage_reading = crank_handler.read()
        print(voltage_reading)

        if voltage_reading > 50:
            audio_player.play()
        else:
            if not audio_player.paused and audio_player.playing:
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
        button_thread = Thread(target=check_button_input)

        loop_thread.start()
        button_thread.start()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

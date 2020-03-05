#!/usr/bin/python3

import time

from audio_player import AudioPlayer
from threading import Thread
from crank_handler import CrankHandler
import RPi.GPIO as GPIO

audio_player = None
crank_handler = None
timer = 2
stop_button = 18
next_button = 17


def setup():
    global audio_player
    global crank_handler
    global stop_button

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(stop_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(next_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    audio_player = AudioPlayer()
    audio_player.load_file()
    crank_handler = CrankHandler()


def check_button_input():
    global stop_button
    global next_button
    global audio_player

    while True:
        stop_button_state = GPIO.input(stop_button)
        next_button_state = GPIO.input(next_button)
        print("Stop button state: ", stop_button_state)
        print("Next button state: ", next_button_state)
        print("Track name: ", audio_player.get_track_name())

        if stop_button_state is 1:
            audio_player.stop()
            time.sleep(1)
        if next_button_state is 1:
            audio_player.next()
            time.sleep(1)

        time.sleep(0.2)


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

        button_thread.start()
        loop_thread.start()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

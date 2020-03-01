import pygame

from audio_player import AudioPlayer
# from crank_handler import CrankHandler

audio_player = AudioPlayer()
audio_player.load_file()
audio_player.play()

while True:
    pass
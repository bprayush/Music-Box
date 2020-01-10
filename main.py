import pygame

pygame.init()
pygame.mixer.music.load('midi/Yellow.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
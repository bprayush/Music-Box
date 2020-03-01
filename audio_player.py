import pygame


class AudioPlayer:

    def __init__(self):
        pygame.init()
        self.playing = False

    @staticmethod
    def load_file(file_name="audio/Yellow.mp3"):
        pygame.mixer.music.load(file_name)

    def play(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True

    @staticmethod
    def get_playing_status():
        return pygame.mixer.music.get_busy()
import pygame


class AudioPlayer:

    def __init__(self):
        self.player = pygame
        self.player.init()
        self.playing = False
        self.paused = False

    def load_file(self, file_name="audio/Jus-the-way-you-are-Music-box.mp3"):
        self.player.mixer.music.load(file_name)

    def play(self):
        if not self.playing:
            if not self.paused:
                print('play')
                self.player.mixer.music.play(loops=-1)
            else:
                print('unpause')
                self.player.mixer.music.unpause()
            self.paused = False
            self.playing = True

    def get_playing_status(self):
        return self.player.mixer.music.get_busy()

    def stop(self):
        self.player.mixer.music.stop()
        self.playing = False
        self.paused = False

    def pause(self):
        print('pause')
        self.player.mixer.music.pause()
        self.playing = False
        self.paused = True

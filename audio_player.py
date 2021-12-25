import pygame


class AudioPlayer:

    def __init__(self):
        self.player = pygame
        self.player.init()
        self.playing = False
        self.paused = False
        self.playerIndex = 0
        self.playerQueue = [
            "audio/Just the way you are- Music Box.mp3",
            "audio/Can't help falling in love -music box.mp3",
            "audio/Yellow -Music Box.mp3",
            "audio/Born to die-Music Box.mp3"
        ]

    def load_file(self):
        audio_file = self.playerQueue[self.playerIndex]
        self.player.mixer.music.load(audio_file)

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

    def next(self):
        self.stop()
        self.playerIndex = (self.playerIndex + 1) % len(self.playerQueue)
        self.load_file()

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

    def get_track_name(self):
        return self.playerQueue[self.playerIndex]

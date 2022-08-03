import pygame
import sys

pygame.init()

class MediaPlayer:



    def __init__(self,sound:str):
        pygame.mixer.init()
        self.sound = sound

        def load_sound(self):
            pygame.mixer.music.load(self.sound)

        pass

    def play(self):
        pass

    def volumeup(self):
        pass

    def volumedown(self):
        pass
    def volumedown(self):
        pass

    def mute(self):
        pass
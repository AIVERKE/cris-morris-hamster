import pygame

pygame.mixer.init()


def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()

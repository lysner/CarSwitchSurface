import pygame

def sound_preview(status):
    pygame.mixer.music.load("audio/on_the_move_carspeed.mp3")
    if status == 1:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()

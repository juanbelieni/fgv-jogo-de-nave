import pygame

pygame.mixer.music.load('src/sound_fx/tracks/main_track.ogg')

pew = pygame.mixer.Sound('src/sound_fx/fx/pew.wav')
pew.set_volume(0.1)

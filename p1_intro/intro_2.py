import pygame
import sys
import os
from src.cercle import Cercle

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Constants
WIDTH = 800
HEIGHT = 480

pygame.init()
ecran = pygame.display.set_mode((WIDTH, HEIGHT))
piano = pygame.mixer.Sound("sons/piano.mp3")
cercle = Cercle((255,0,0))

def gererFermeture():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    gererFermeture()
    ecran.fill((0, 0, 0))
    cercle.verifierX(ecran)
    pygame.display.flip()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        piano.play()
    



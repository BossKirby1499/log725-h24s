import pygame
from src.forme import Forme

class Cercle(Forme):
<<<<<<< HEAD
    rayon = 100
=======
    rayon = 10
>>>>>>> 45ab958471d2af8d7aaa1c380e04081740d8abf5

    def __init__(self, couleur):
        Forme.__init__(self, couleur)

    def retournerOriginal(self):
        if self.rayon > 10:
<<<<<<< HEAD
            self.rayon -= 10
=======
            self.rayon -= 1
>>>>>>> 45ab958471d2af8d7aaa1c380e04081740d8abf5
        else:
            self.rayon = 10

    def verifierX(self, ecran):
<<<<<<< HEAD
        #ecran.fill((0, 0, 0))
        self.verifierEspace()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            self.rayon += 10
        else:
            self.retournerOriginal()
        print(self.rayon)

        pygame.draw.circle(ecran, self.couleur, (200, 200), self.rayon, 0)
=======
        self.verifierEspace()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            self.rayon += 1
        else:
            self.retournerOriginal()
        pygame.draw.circle(ecran, self.couleur, (200, 200), self.rayon, 0)
        pygame.display.flip()
        ecran.fill((0,0,0))
>>>>>>> 45ab958471d2af8d7aaa1c380e04081740d8abf5

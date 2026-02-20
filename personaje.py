import pygame

class Personaje():
    def __init__(self,x,y):
        self.shape = pygame.Rect(0,0,20,20)
        self.shape.center = (x,y)
        
    def draw(self, ventana):
        pygame.draw.rect(ventana, (255,255,0), self.shape)
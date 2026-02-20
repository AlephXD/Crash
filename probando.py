import os
import pygame 
import cons

pygame.init()

ventana = pygame.display.set_mode((cons.ancho,cons.alto))
pygame.display.set_caption("CRASH")

#Crear tablero

dir_tablero= os.path.join('assets', 'tablero.png')
tablero= pygame.image.load(dir_tablero).convert_alpha()
tablero = pygame.transform.scale(tablero,(600,600))

#Carritos

dir_carrito= os.path.join('assets', 'rojo.png')
pj = pygame.image.load(dir_carrito).convert_alpha()
pj = pygame.transform.scale(pj, (150,150))

    
run = True

while run:
    ventana.fill(cons.color_bg)
    
    ventana.blit(tablero, (360,50))
    ventana.blit(pj, (400,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

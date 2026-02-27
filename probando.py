import pygame 
import cons
from cars import *

pygame.init()

ventana = pygame.display.set_mode((cons.ancho,cons.alto))
pygame.display.set_caption("CRASH")

#Crear tablero

dir_tablero= "assets//tablero.png"
tablero= pygame.image.load(dir_tablero).convert_alpha()
tablero = pygame.transform.scale(tablero,(600,600))

#Limites del tablero
linea_w=pygame.Rect(360,10,700,90)
linea_a=pygame.Rect(360,10,45,700)
linea_d=pygame.Rect(920,10,50,700)
linea_s=pygame.Rect(360,610,700,50)

muro_r = [ linea_a, linea_d, linea_w, linea_s]
muro_v = [ linea_a, linea_d, linea_w, linea_s]
muro_c = [ linea_a, linea_d, linea_w, linea_s]
#Carritos
act_car= None
carros = []
dir_rojo= pygame.image.load("assets//rojo2.png").convert_alpha()
dir_rojo = pygame.transform.scale(dir_rojo, (150,80))
dir_verde = pygame.image.load("assets//autoverde2.png").convert_alpha()
dir_verde = pygame.transform.scale(dir_verde,(80,150)).convert_alpha()
dir_camion = pygame.image.load("assets//camion2.png").convert_alpha()
dir_camion = pygame.transform.scale(dir_camion,(80,250)).convert_alpha()
camion_r = vehiculo(875, 225, dir_camion, muro_c, 'v')
verde = vehiculo(445,180, dir_verde, muro_v,  'v')
rojo= vehiculo(490,315, dir_rojo, muro_r,   'h')
muro_r.append(verde.forma)
muro_r.append(camion_r.forma)
muro_v.append(camion_r.forma)
muro_v.append(rojo.forma)
muro_c.append(rojo.forma)
muro_c.append(verde.forma)
carros.append(rojo)
carros.append(verde)
carros.append(camion_r)

run = True
#loop principal
while run:
    col = cons.white
    #Dibujando
    ventana.fill(cons.color_bg)
    ventana.blit(tablero, (360,50))
    rojo.dibujar(ventana)
    verde.dibujar(ventana)
    camion_r.dibujar(ventana)
    pygame.draw.rect(ventana, cons.white, linea_w)
    
    pygame.draw.rect(ventana, cons.white, linea_d)
    pygame.draw.rect(ventana, cons.white, linea_s)
    
    
    
    #Manejador de eventos
    for event in pygame.event.get():
        
        #Agarrar
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, carro in enumerate(carros):
                    if carro.forma.collidepoint(event.pos):
                        act_car = num
                       
                        
        #Soltar
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                act_car = None
        
        #Mover junto al mouse
        if event.type == pygame.MOUSEMOTION:
            if act_car != None:
                if carros[act_car].sen == 'h':
                    old_pos = carros[act_car].forma.topleft
                    carros[act_car].forma.move_ip(event.rel[0], 0)
                    for colision in carros[act_car].muros:
                        if carros[act_car].forma.colliderect(colision):
                         carros[act_car].forma.topleft = old_pos
                elif carros[act_car].sen == 'v':
                    old_pos = carros[act_car].forma.topleft
                    carros[act_car].forma.move_ip(0, event.rel[1])
                    for colision in carros[act_car].muros:
                        if carros[act_car].forma.colliderect(colision):
                         carros[act_car].forma.topleft = old_pos
                         
                    
                
                
        if event.type == pygame.QUIT:
            run = False
    
    
    pygame.display.update()

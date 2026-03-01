import pygame, sys
from botones import Boton

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Crash")
fondo = pygame.image.load("assets//PortadaFinal.png").convert()
jugar = Boton("assets//BotonJugar.png", "Sonido//Click.mp3", (550, 345), 0.1)
niveles = Boton("assets//BotonNiveles.png", "Sonido//Click.mp3", (550, 445), 0.1)
salir = Boton("assets//BotonSalirRojo.png", "Sonido//Click.mp3", (550, 545), 0.1)
pygame.mixer.music.load("Sonido//Sonidomenu.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if jugar.es_presionado():
            print("Boton jugar presionado")

        if niveles.es_presionado():
            print("Elija el nivel")

        if salir.es_presionado():
            pygame.quit()
            sys.exit()


    screen.fill("black")
    screen.blit(fondo, (0, 0))
    jugar.draw(screen)
    niveles.draw(screen)
    salir.draw(screen)

    pygame.display.flip()

    clock.tick(60)

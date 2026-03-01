import pygame

from botones import Boton
from pathlib import Path
from cars import vehiculo, pj
from enfocate import GameBase, GameMetadata, COLORS

class Game(GameBase):
    
    
    def __init__(self):
        
        meta = GameMetadata(
            title= "Crash",
            description="Puzzle de autos, donde deberas correctamente posicionarlos para llevar tu auto a la salida",
            authors=["Alexandro Nunez", "Carlos Pachecho", "Victor Coa", "Jesus Mata"],
            group_number=2
        )
        
        super().__init__(meta)
        
        self.puntuacion=0 
        
        self.estado = 'start'
        self.estado_prev = None
        self.moviendo = False
        self.cood = ()
        lw=pygame.Rect(360,10,700,90)
        la=pygame.Rect(360,10,45,700)
        ld=pygame.Rect(920,10,50,700)
        ls=pygame.Rect(360,610,700,50)
        self.ganar=pygame.Rect(840, 280, 60,60)
        self.muros = [lw, la, ld, ls]
        self.act_car = None
        self.load = False
        self.salir = False
     
    def on_start(self):
        
        self.tablero = pygame.image.load(Path("assets")/"tablero.png").convert_alpha()
        self.tablero = pygame.transform.scale(self.tablero,(600,600))
        
        self.dir_click= Path("Sonido")/"Click.mp3"
        self.fondo = pygame.image.load("assets//PortadaFinal.png").convert()

        pygame.mixer.music.load(Path("Sonido")/"Sonidomenu.mp3")
        pygame.mixer.music.play(-1)
        
        return super().on_start()
        
    
    def victoria(self):
        print("has ganado")
    def autos(self):
        self.camion_r = vehiculo((0, 0), Path("assets")/ "CamionAzul2.png", (80,250), [], 'v')
        self.morado = vehiculo((0, 0), Path("assets")/ "Automorado2.png",(80,150), [],  'v')
        self.rojo= pj((0,0), Path("assets")/ "rojo2.png",(150,80), [],   'h', self.ganar)
        self.negro= vehiculo((0,0), Path("assets")/ "CKcar2.png",(150,80), [],   'h')
        self.gris= vehiculo((0,0), Path("assets")/ "Autogris2.png",(150,80), [],   'h')
        self.naranja = vehiculo((0, 0), Path("assets")/ "AutoNaranja2.png",(80,150),[],  'v')
        self.camion_v = vehiculo((0, 0), Path("assets")/ "CamionVerde2.png", (80,250), [], 'v')
        self.carros = [self.morado,self.camion_r,self.rojo, self.negro,self.gris,self.naranja, self.camion_v]
        for iterar in self.carros:
            iterar.carros.extend(self.carros)
        
    def boton(self):
        
        if self.estado == 'start':
            self.jugar =  Boton(Path("assets")/ "BotonJugar.png", self.dir_click, (550, 345), 0.1)
            if self.jugar.es_presionado():
                self.estado_prev = self.estado
                self.estado = 'nivel1'
                self.load = True
                self.jugar.sound.play()
            self.niveles = Boton(Path("assets")/"BotonNiveles.png", Path("Sonido")/"Click.mp3", (550, 445), 0.1)
            if self.niveles.es_presionado():
                self.estado_prev = self.estado
                self.estado = 'nivel1'
                
                self.jugar.sound.play()
            self.salir = Boton(Path("assets")/"BotonSalirRojo.png", Path("Sonido")/"Click.mp3", (550, 545), 0.1)
            if self.salir.es_presionado():
                self.jugar.sound.play()
                self._stop_context()
            self.reiniciar = Boton(Path("assets")/"BotonReiniciar.png", Path("Sonido")/"Click.mp3", (150, 545), 0.1)
                
    def update(self, dt: float):
        if self.estado == 'start':
            self.boton()
            self.autos()
        
        #NIVEL1#
        if self.estado == 'nivel1' and self.load == True:
            self.rojo.forma.center = (580,315)
            self.morado.forma.center = (530, 520)
            self.camion_r.forma.center= (875, 480)
            self.negro.forma.center= (580,405)
            self.gris.forma.center= (650,570)
            self.camion_v.forma.center= (700,405)
            self.load = False
        
        if self.estado != 'start' or 'niveles':
            self.boton()
    
        if self.moviendo:
            if self.act_car is None:
                self.moviendo = False
                return 
            if self.carros[self.act_car].sen == 'h':
                old_pos = self.carros[self.act_car].forma.topleft
                self.carros[self.act_car].forma.move_ip(self.cood[0], 0)
                for colision in self.muros:
                    if self.carros[self.act_car].forma.colliderect(colision):
                        self.carros[self.act_car].forma.topleft = old_pos
                
                for colision in self.carros[self.act_car].carros:
                    if colision != self.carros[self.act_car] and self.carros[self.act_car].forma.colliderect(colision.forma):
                        self.carros[self.act_car].forma.topleft = old_pos
                
                if self.carros[self.act_car] == self.rojo:
                        if self.carros[self.act_car].forma.colliderect(self.carros[self.act_car].victoria):
                            self.victoria()
                            
            elif self.carros[self.act_car].sen == 'v':
                old_pos = self.carros[self.act_car].forma.topleft
                self.carros[self.act_car].forma.move_ip(0, self.cood[1])
                
                for colision in self.muros:
                    if self.carros[self.act_car].forma.colliderect(colision):
                        self.carros[self.act_car].forma.topleft = old_pos
                
                
                for colision in self.carros[self.act_car].carros:
                    if colision != self.carros[self.act_car] and self.carros[self.act_car].forma.colliderect(colision.forma):
                        self.carros[self.act_car].forma.topleft = old_pos
            self.moviendo = False
        pass
           
    def handle_events(self, events: list[pygame.event.Event]):
        
        for event in events:
                if event.type == pygame.QUIT:
                    self._stop_context()
                #Agarrar
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for num, carro in enumerate(self.carros):
                            if carro.forma.collidepoint(event.pos):
                                self.act_car = num
                                
                        if self.reiniciar.es_presionado():
                            self.reiniciar.sound.play()
                            self.load = True
    
                        
                #Soltar
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.act_car = None
        
        #Mover junto al mouse
                if event.type == pygame.MOUSEMOTION:
                    if self.act_car != None:
                        self.cood = event.rel
                        self.moviendo = True
                    
                                            
                
        
        return super().handle_events(events)   
       
            
    def draw(self):
        
        if self.estado == 'start':
            self.surface.blit(self.fondo, (0,0))
            self.surface.blit(self.jugar.image, self.jugar.rect)
            self.surface.blit(self.niveles.image, self.niveles.rect)
            self.surface.blit(self.salir.image, self.salir.rect)
            
        if self.estado == 'nivel1':
            self.surface.blit(self.fondo, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.morado.image, self.morado.forma)
            self.surface.blit(self.camion_r.image, self.camion_r.forma)
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.gris.image, self.gris.forma )
            self.surface.blit(self.camion_v.image, self.camion_v.forma )
            self.surface.blit(self.reiniciar.image, self.reiniciar.rect)

        
if __name__ == '__main__':
    Game().run_preview()

import pygame

from botones import Boton
from pathlib import Path
from cars import vehiculo
from enfocate import GameBase, GameMetadata, COLORS

SCREENWIDTH, SCREENHEIGHT = 1280, 720
FPS = 60
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
        
        lw=pygame.Rect(360,10,700,90)
        la=pygame.Rect(360,10,45,700)
        ld=pygame.Rect(920,10,50,700)
        ls=pygame.Rect(360,610,700,50)
        self.mr = self.mv = self.mcr = self.ma = self.mca = self.mcv = self.mg = [lw, la, ld, ls]
        self.act_car= None
     
    def on_start(self):
        
        self.tablero = pygame.image.load(Path("assets")/"tablero.png").convert_alpha()
        self.tablero = pygame.transform.scale(self.tablero,(600,600))
        self.camion_r = vehiculo('camionr',(0, 0), Path("assets")/ "camion2.png", (0,0), self.mcr, 'v')
        self.verde = vehiculo('verde',(0,0), Path("assets")/ "autoverde2.png",(0,0), self.mv,  'v')
        self.rojo= vehiculo('rojo',(0,0), Path("assets")/ "rojo2.png",(0,0), self.mr,   'h')
        dir_jugar= Path("assets")/ "BotonJugar.png"
        dir_click= Path("Sonido")/"Click.mp3"
        self.jugar =  Boton(dir_jugar, dir_click, (550, 345), 0.1)
        self.fondo = pygame.image.load("assets//PortadaFinal.png").convert()
        self.carros = [self.verde,self.camion_r,self.rojo]
        self.niveles = Boton(Path("assets")/"BotonNiveles.png", Path("Sonido")/"Click.mp3", (550, 445), 0.1)
        self.salir = Boton(Path("assets")/"BotonSalirRojo.png", Path("Sonido")/"Click.mp3", (550, 545), 0.1)
        pygame.mixer.music.load(Path("Sonido")/"Sonidomenu.mp3")
        pygame.mixer.music.play(-1)
        return super().on_start()
        
    def update(self, dt: float):
        
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
                       
                        
                #Soltar
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.act_car = None
        
        #Mover junto al mouse
                if event.type == pygame.MOUSEMOTION:
                    if self.act_car != None:
                        if self.carros[self.act_car].sen == 'h':
                            old_pos = self.carros[self.act_car].forma.topleft
                            self.carros[self.act_car].forma.move_ip(event.rel[0], 0)
                            for colision in self.carros[self.act_car].muros:
                                if self.carros[self.act_car].forma.colliderect(colision):
                                    self.carros[self.act_car].forma.topleft = old_pos
                        elif self.carros[self.act_car].sen == 'v':
                            old_pos = self.carros[self.act_car].forma.topleft
                            self.carros[self.act_car].forma.move_ip(0, event.rel[1])
                            for colision in self.carros[self.act_car].muros:
                                if self.carros[self.act_car].forma.colliderect(colision):
                                    self.carros[self.act_car].forma.topleft = old_pos
                                            
                if self.jugar.es_presionado():
                    self.estado_prev = self.estado
                    self.estado = 'nivel1'
                    self.jugar.sound.play()
        
        return super().handle_events(events)   
       
            
    def draw(self):
        
        if self.estado == 'start':
            self.surface.blit(self.fondo, (0,0))
            self.surface.blit(self.jugar.image, self.jugar.rect)
            self.surface.blit(self.niveles.image, self.niveles.rect)
            self.surface.blit(self.salir.image, self.salir.rect)
            
        if self.estado == 'nivel1':
            self.camion_r.cambiar((875, 225), Path("assets")/ "camion2.png", (80,250), 'v')
            self.rojo.cambiar((490,315), Path("assets")/ "rojo2.png", (150,80), 'h')
            self.verde.cambiar((445, 180), Path("assets")/ "autoverde2.png", (80,150), 'v')
            self.surface.blit(self.fondo, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.verde.image, self.verde.forma)
            self.surface.blit(self.camion_r.image, self.camion_r.forma)
        
              

        
if __name__ == '__main__':
    Game().run_preview()

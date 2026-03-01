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
        self.cargar_nivel = False
        self.click = False
        self.cargarbtn = True
        self.dibujar = False
        self.signiv = None
    def on_start(self):
        
        self.tablero = pygame.image.load(Path("assets")/"tablero.png").convert_alpha()
        self.tablero = pygame.transform.scale(self.tablero,(600,600))
        self.cartelvic =  pygame.image.load(Path("assets")/"victoria.png").convert_alpha()
        self.dir_click= Path("Sonido")/"Click.mp3"
        self.fondo = pygame.image.load(Path("assets")/"PortadaFinal.png").convert()
        self.gameplay = pygame.image.load(Path("assets")/"portadaJuego.png").convert()
        self.fanfare = pygame.mixer.Sound(Path("Sonido")/"Victoria.mp3")
        self.agarrar = pygame.mixer.Sound(Path("Sonido")/"Agarrar.mp3")
        self.facil = pygame.image.load(Path("assets")/"Facil.png").convert_alpha()
        self.facil = pygame.transform.scale(self.facil, (200,100))
        self.normal = pygame.image.load(Path("assets")/"Normal.png").convert_alpha()
        self.normal= pygame.transform.scale(self.normal, (200,100))

        
        
        return super().on_start()
        
    
    def victoria(self):
        self.fanfare.play()
        self.estado = 'victoria'
        
        
    def autos(self):
        self.camion_r = vehiculo((0, 0), Path("assets")/ "camion2.png", (80,250), [], 'v')
        self.camion_ama = vehiculo((0, 0), Path("assets")/ "CamionAmarillo.png", (80,250), [], 'v')
        self.camion_azuh = vehiculo((0, 0), Path("assets")/ "CamionAzul3.png", (250,80), [], 'h')
        self.morado = vehiculo((0, 0), Path("assets")/ "Automorado2.png",(80,150), [],  'v')
        self.morado_h = vehiculo((0, 0), Path("assets")/ "Automorado3.png",(150,80),[],  'h')
        self.rojo= pj((0,0), Path("assets")/ "rojo2.png",(150,80), [],   'h', self.ganar)
        self.negro= vehiculo((0,0), Path("assets")/ "CKcar2.png",(150,80), [],   'h')
        self.gris= vehiculo((0,0), Path("assets")/ "Autogris2.png",(150,80), [],   'h')
        self.naranja = vehiculo((0, 0), Path("assets")/ "AutoNaranja2.png",(80,150),[],  'v')
        self.naranja_h = vehiculo((0, 0), Path("assets")/ "AutoNaranja3.png",(150,80),[],  'h')
        self.camion_v = vehiculo((0, 0), Path("assets")/ "CamionVerde2.png", (80,250), [], 'v')
        self.negro_v= vehiculo((0,0), Path("assets")/ "CKcar3.png",(80,150), [],   'v')
        self.gris_v= vehiculo((0,0), Path("assets")/ "Autogris3.png",(80,150), [],   'v')
        self.taxi_v= vehiculo((0,0), Path("assets")/ "Taxi3.png",(80,150), [],   'v')
        self.taxi= vehiculo((0,0), Path("assets")/ "Taxi2.png",(150,80), [],   'h')
        self.verde= vehiculo((0,0), Path("assets")/ "autoverde2.png",(80,150), [],   'v')
        self.verde_h= vehiculo((0,0), Path("assets")/ "autoverde3.png",(150,80), [],   'h')
        self.camion_vh = vehiculo((0, 0), Path("assets")/ "CamionVerde3.png", (250,80), [], 'h')
        self.carros = [self.camion_azuh,self.camion_ama,self.verde_h,self.morado_h,self.naranja_h,self.morado,self.camion_r,self.rojo, self.negro,self.gris,self.naranja, self.camion_v, self.negro_v,self.gris_v, self.taxi_v, self.verde, self.camion_vh, self.taxi]
        for iterar in self.carros:
            iterar.carros.extend(self.carros)
            
    def boton(self):
        
        if self.estado == 'start':
            if self.click == True:
                if self.jugar.es_presionado():
                    self.estado = 'nivel1'
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    self.load = True
                    self.cargarbtn = True
                    self.nivel = True
                    pygame.mixer.music.load(Path("Sonido")/"jugar.wav")
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
            
                    
                if self.salir.es_presionado():
                    self._stop_context()
            self.click = False
        
        if self.estado == 'victoria':
            if self.click == True:
                if self.siguiente.es_presionado():
                    self.load = True
                    self.estado = self.signiv
            self.click = False
            
        
        
        if self.estado != 'start' and self.estado != 'niveles'and self.estado != 'victoria':
            if self.click == True:
                if self.reiniciar.es_presionado():
                    self.load = True
                    self.cargarbtn = True
                
                
                if self.salirnivel.es_presionado():
                    self.estado = 'start'
                    self.cargarbtn = True
                    self.dibujar = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    
            self.click = False
                
        

        
    def cargarbotones(self):
            
        if self.estado == 'start':
            self.jugar =  Boton(Path("assets")/ "BotonJugar.png", self.dir_click, (550, 345), 0.1)
            self.niveles = Boton(Path("assets")/"BotonNiveles.png", Path("Sonido")/"Click.mp3", (550, 445), 0.1)
            self.salir = Boton(Path("assets")/"BotonSalirRojo.png", Path("Sonido")/"Click.mp3", (550, 545), 0.1)
            
        if self.estado != 'start' and self.estado != 'niveles' and self.estado != 'victoria':
            self.reiniciar = Boton(Path("assets")/"BotonReiniciar.png", Path("Sonido")/"Click.mp3", (150, 545), 0.1)
            
        if self.estado != 'start' and  self.estado != 'victoria':
            self.salirnivel = Boton(Path("assets")/"BotonSalirNivel.png", Path("Sonido")/"Click.mp3", (150, 445), 0.1)
        if self.estado == 'victoria':
            self.siguiente = Boton(Path("assets")/"Botonsiguiente.png", Path("Sonido")/"Click.mp3", (550, 545), 0.1)
            


        

            
        
    def update(self, dt: float):

            
        if self.estado == 'victoria' and self.cargarbtn == True:
            self.cargarbotones()
            self.cargarbtn = False
            self.dibujar = True
        if self.estado == 'start' and self.cargarbtn == True:
            self.nivel = False
            pygame.mixer.music.load(Path("Sonido")/"Sonidomenu.wav")
            pygame.mixer.music.set_volume(0.3)
            self.cargarbotones()
            pygame.mixer.music.play(-1)
            self.autos()
            self.cargarbtn = False
        

        if self.estado != 'start' and self.estado != 'niveles' and self.estado != 'victoria' and self.cargarbtn == True:
            self.cargarbotones()
            self.cargarbtn = False
            self.dibujar= True
            
        if self.estado != 'start'  and self.estado != 'victoria' and self.cargarbtn == True:
            self.cargarbotones()
            self.cargarbtn = False
            self.dibujar = True
    
        #NIVEL1
        if self.estado == 'nivel1' and self.load == True:
            self.autos()
            self.rojo.forma.center = (580,315)
            self.morado.forma.center = (530, 520)
            self.camion_r.forma.center= (875, 480)
            self.negro.forma.center= (580,405)
            self.gris.forma.center= (650,570)
            self.camion_v.forma.center= (700,405)
            self.signiv = 'nivel2'
            self.load = False
            
        #NIVEL2
        
        if self.estado == 'nivel2' and self.load == True:
            self.autos()
            self.rojo.forma.center = (580,315)
            self.negro.forma.center= (670,405)
            self.morado.forma.center = (700, 270)
            self.taxi_v.forma.center = (700, 530)
            self.naranja.forma.center = (535,180)
            self.gris.forma.center = (650,140)
            self.gris_v.forma.center = (870, 180)
            self.negro_v.forma.center = (790, 180)
            self.verde.forma.center = (870, 350)
            self.signiv = 'nivel3'
            self.load = False
            
        #NIVEL3 
        
        if self.estado == 'nivel3' and self.load == True:
            self.autos()
            self.rojo.forma.center = (580,315)
            self.naranja.forma.center = (620,180)
            self.camion_vh.forma.center = (625,400)
            self.camion_r.forma.center = (445,405)
            self.camion_v.forma.center = (870,315)
            self.gris.forma.center = (820,140)
            self.negro.forma.center = (820,480)
            self.taxi.forma.center = (820,570)
            self.morado.forma.center = (700,530)
            self.morado_h.forma.center = (500,225)
            self.naranja_h.forma.center = (500,145)
            self.verde_h.forma.center = (490,570)
            self.signiv = 'nivel4'
            self.load = False
            
        if self.estado == 'nivel4' and self.load == True:
            self.autos()
            self.rojo.forma.center = (760,315)
            self.camion_v.forma.center = (870,230)
            self.negro_v.forma.center = (790, 180)
            self.gris.forma.center = (650,140)
            self.negro.forma.center = (650,222)
            self.camion_r.forma.center= (618,405)
            self.naranja_h.forma.center = (500,145)
            self.verde_h.forma.center = (490,570)
            self.gris_v.forma.center = (535, 355)
            self.morado.forma.center = (455, 261)
            self.camion_vh.forma.center = (787,400)
            self.signiv = 'nivel5'
            self.load = False
            
        if self.estado == 'nivel5' and self.load == True:
            self.autos()
            self.rojo.forma.center = (580,315)
            self.camion_r.forma.center = (706,230)
            self.gris.forma.center = (568,140)
            self.camion_ama.forma.center = (450,230)
            self.camion_vh.forma.center = (787,400)
            self.camion_azuh.forma.center = (706,562)
            self.naranja.forma.center = (620,445)
            self.taxi_v.forma.center = (870, 525)
            
            self.signiv = 'nivel6'
            self.load = False
            
        if self.estado == 'nivel6' and self.load == True:
            self.autos()
            self.rojo.forma.center = (499,315)
            self.camion_r.forma.center = (625,230)
            self.naranja.forma.center = (535,180)
            self.camion_vh.forma.center = (625,400)
            self.morado.forma.center = (449, 439)
            self.gris_v.forma.center = (700,530)
            self.negro.forma.center= (580,486)
            self.taxi.forma.center = (820,570)
            self.verde_h.forma.center = (820,140)
            self.naranja_h.forma.center = (820,222)
            self.camion_v.forma.center = (870,396)

            self.signiv = 'start'
            self.load = False
    
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
                            self.dibujar = False
                            self.cargarbtn = True
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
        self.boton()
        
           
    def handle_events(self, events: list[pygame.event.Event]):
        
        for event in events:
                if event.type == pygame.QUIT:
                    self._stop_context()
                #Agarrar
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                        for num, carro in enumerate(self.carros):
                            if carro.forma.collidepoint(event.pos):
                                self.agarrar.play()
                                self.act_car = num
                        
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
            self.surface.blit(self.salir.image, self.salir.rect)
            

        if self.estado == 'nivel1':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.morado.image, self.morado.forma)
            self.surface.blit(self.camion_r.image, self.camion_r.forma)
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.gris.image, self.gris.forma )
            self.surface.blit(self.camion_v.image, self.camion_v.forma )
            
        if self.estado == 'nivel2':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.morado.image, self.morado.forma)
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.naranja.image, self.naranja.forma )
            self.surface.blit(self.gris.image, self.gris.forma)
            self.surface.blit(self.taxi_v.image, self.taxi_v.forma)
            self.surface.blit(self.gris_v.image, self.gris_v.forma)
            self.surface.blit(self.negro_v.image, self.negro_v.forma)
            self.surface.blit(self.verde.image, self.verde.forma)
            
        if self.estado == 'nivel3':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.naranja.image, self.naranja.forma )
            self.surface.blit(self.camion_vh.image, self.camion_vh.forma )
            self.surface.blit(self.camion_r.image, self.camion_r.forma )
            self.surface.blit(self.camion_v.image, self.camion_v.forma )
            self.surface.blit(self.gris.image, self.gris.forma)
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.taxi.image, self.taxi.forma )
            self.surface.blit(self.morado.image, self.morado.forma )
            self.surface.blit(self.morado_h.image, self.morado_h.forma )
            self.surface.blit(self.naranja_h.image, self.naranja_h.forma )
            self.surface.blit(self.verde_h.image, self.verde_h.forma )
            
        if self.estado == 'nivel4':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.camion_v.image, self.camion_v.forma )
            self.surface.blit(self.negro_v.image, self.negro_v.forma )
            self.surface.blit(self.gris.image, self.gris.forma )
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.camion_r.image, self.camion_r.forma )
            self.surface.blit(self.naranja_h.image, self.naranja_h.forma )
            self.surface.blit(self.verde_h.image, self.verde_h.forma )
            self.surface.blit(self.gris_v.image, self.gris_v.forma )
            self.surface.blit(self.morado.image, self.morado.forma )
            self.surface.blit(self.camion_vh.image, self.camion_vh.forma )
            
        if self.estado == 'nivel5':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.camion_r.image, self.camion_r.forma )
            self.surface.blit(self.gris.image, self.gris.forma )
            self.surface.blit(self.camion_ama.image, self.camion_ama.forma )
            self.surface.blit(self.camion_vh.image, self.camion_vh.forma )
            self.surface.blit(self.camion_azuh.image, self.camion_azuh.forma )
            self.surface.blit(self.naranja.image, self.naranja.forma )
            self.surface.blit(self.taxi_v.image, self.taxi_v.forma )
            
        if self.estado == 'nivel6':
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.tablero, (360,50))
            self.surface.blit(self.rojo.image, self.rojo.forma )
            self.surface.blit(self.camion_r.image, self.camion_r.forma )
            self.surface.blit(self.naranja.image, self.naranja.forma )
            self.surface.blit(self.camion_vh.image, self.camion_vh.forma )
            self.surface.blit(self.morado.image, self.morado.forma )
            self.surface.blit(self.gris_v.image, self.gris_v.forma )
            self.surface.blit(self.negro.image, self.negro.forma )
            self.surface.blit(self.taxi.image, self.taxi.forma )
            self.surface.blit(self.verde_h.image, self.verde_h.forma )
            self.surface.blit(self.naranja_h.image, self.naranja_h.forma )
            self.surface.blit(self.camion_v.image, self.camion_v.forma )
            
        if self.estado != 'start' and self.estado != 'niveles' and self.estado != 'victoria' and self.dibujar == True:
            self.surface.blit(self.reiniciar.image, self.reiniciar.rect)
            self.surface.blit(self.salirnivel.image, self.salirnivel.rect)
            
            
            
        
        if self.estado == 'victoria' and self.dibujar == True:
            self.surface.blit(self.gameplay, (0,0))
            self.surface.blit(self.cartelvic, (430,120))
            self.surface.blit(self.siguiente.image, self.siguiente.rect)


        
if __name__ == '__main__':
    Game().run_preview()

import pygame

class vehiculo():
    def __init__(self, x, y,image, muros,  sen):
        self.sen = sen
        self.muros = muros
        self.image = image
        self.forma= self.image.get_rect(center=(x,y))  
        
    def update(self, x,y):
        if self.sen == 'h':
         lista_colisiones = self.colisiones
         for colisionable in lista_colisiones:
            if (x > 0):
                self.forma.right = colisionable.left
                
            elif (x < 0):
                self.forma.left = colisionable.right
        
        elif self.sen == 'v':
        
         lista_colisiones = self.colisiones
         for colisionable in lista_colisiones:
            if (y > 0):
                self.forma.bottom = colisionable.top
                
            elif (y < 0):
                self.forma.top = colisionable.bottom
        
            
                
        
    def dibujar(self, ventana):
        ventana.blit(self.image, self.forma)
        
        
        
     
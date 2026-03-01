import pygame

class vehiculo():
    def __init__(self, posicion,image, escala, carros,  sen):
        self.carros= carros
        self.sen = sen
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, escala)
        self.forma= self.image.get_rect(center=(posicion)) 
        
    

class pj(vehiculo):
    def __init__(self,posicion,image, escala, carros, sen, victoria):
        super().__init__(posicion, image, escala, carros, sen)
        self.victoria = victoria
            
            
        
        
        
     
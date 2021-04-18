import pygame, sys
from pygame.locals import *

class mainApp():
    # Creamos los 3 atributos
    termometro = None
    entrada = None
    selector = None
    # Inicializamos el constructor
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__screen.fill((244, 236, 203))
        
    def __on_close(self):
        pygame.quit()
        sys.exit()    
    
    def start(self): # Genero un método start, que es que la aplicación se lance
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            pygame.display.flip() # Esto es el renderizado. Pintarlo.
        
    
        
if __name__ == '__main__':
    pygame.init()
    app = mainApp() # La aplicación va a ser una instancia de mainApp
    app.start() # Me meto en el bucle principal de la instancia. Lanzo la instancia por así decirlo

        
        

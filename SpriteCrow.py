# LEONARDO LUNA, ANIMACIÓN DE LOS SPRITES, 12/ 08 / 2023 
from pygame import *  
import pygame, sys 


class Player(pygame.sprite.Sprite): 
    def __init__(self, pos_x, pos_y): 
        super().__init__()
        self.sprites = []
        self.is_animating = False # Se inicializa a la animación como una entidad falsa, por lo tanto muestra una imagen estática
        # Primera animación, Cuervo quieto 
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow0.png')) # Agregar el nombre del sprite que será importado
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow1.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow2.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow3.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow4.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow5.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow6.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow7.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow8.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow9.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow10.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow11.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))

        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))

        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))

        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))

        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))


        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow12.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow13.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow14.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow15.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow16.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow17.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow18.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow19.png'))


        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow20.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow21.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow22.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow23.png'))
        self.sprites.append(pygame.image.load('../LINK/Graphics/spritecrow/Crow24.png'))


        
        





        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite] 

        self.rect = self.image.get_rect() 
        self.rect.topleft = [pos_x,pos_y]
        
    

        # Dependiendo de la cantidad de imagenes (fotogramas) para realizar la animación 
        # se coloca como instrucción la siguiente línea
        # self.sprites.append(pygame.image.load('')) 


       # self.image = pygame.Surface([20,20])
       # self.image.fill((255,255,255)) 
       # self.rect = self.image.get_rect() 
       # self.rect.topleft = [pos_x,pos_y]
    
    def animate(self):
        self.is_animating = True




    def update(self,speed):
        if self.is_animating == True: 
            self.current_sprite += 0.18 #speed # 1, Se cambia este valor a uno menor que 1, con está línea se controla la velocidad de animación 
        

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False # Ahora la animación comienza y se detiene inmediatamente

        #self.image = self.sprites[self.current_sprite]
        self.image = self.sprites[int(self.current_sprite)]
        # Ejecute el programa en esta parte, y en teoría ya funciona, el problema es que los 
        # sprites se mueven demasiado rápido, de manera que el código no funciona de la manera en la que esperamos que lo haga
        # adecuadamente 


# Configuración general
pygame.init() 
clock = pygame.time.Clock() 

# Pantalla del juego
screen_width = 400 
screen_height = 400 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CROW FLY")

# Creación de los sprites y los grupos
moving_sprites = pygame.sprite.Group() 
player = Player(10,10)
moving_sprites.add(player)

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 

    # Creando la entrada para lograr que la animación comience a moverse 
        if event.type == pygame.KEYDOWN:
            player.animate() 


    # Dibujando 
    screen.fill((0,0,0))
    screen.fill('white')


    moving_sprites.draw(screen)
    moving_sprites.update(0.05) # Se llama al método de actualización en cada uno de los sprites,de está manera conseguimos la animación del grupo de imagenes 
    pygame.display.flip() 
    clock.tick(60) 

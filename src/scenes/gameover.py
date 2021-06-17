import pygame

from src.objects.background import Background
from src.sprites import sprites

# Game over font 
txt='Pressione qualquer tecla para continuar...'                                
pygame.font.init()                               
fonte=pygame.font.get_default_font()              
fontesys=pygame.font.SysFont(fonte, 30) 

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
    
        width, height = self.screen.get_size()  
        self.size_x, self.size_y = 400, 400 
        self.X = width/2 - self.size_x/2
        self.Y = height/2 - self.size_y/2  

        self.image = pygame.transform.scale(sprites.game_over, ((self.size_x), (self.size_y)))
        self.over_text = fontesys.render(txt, 1, (80,0,0))
        
    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000,600), pygame.SRCALPHA)  
        s.fill((0,0,0,180))        # valor de alpha sobre a cor 
        self.screen.blit(s, (0,0))
        self.screen.blit(self.image, (self.X-20, self.Y))
        self.screen.blit(self.over_text,(280,500) )
        
        
    def update(self,dt):
        self.background.update(dt)





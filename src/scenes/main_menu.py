import pygame

from src.sprites import sprites
from src.scenes.scene import Scene
from src.objects.background import Background

class MenuScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.width, self.height = self.screen.get_size()
        self.mid_w, self.mid_h = self.width/2, self.height/2
        self.state = "Start"
        self.cursor_rect = pygame.Rect(0, 0, 80, 80)
        self.offset = -200
        self.font_name = 'src/Fonte_do_game.TTF'
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.startx, self.starty = self.mid_w, self.mid_h - 30
        self.instructionsx, self.instructionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 130
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        
    def draw_cursor(self):
        self.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y)
    
    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))

        self.draw_text('MENU INICIAL', 35, self.mid_w, self.mid_h - 160)
        self.draw_text("ESTOU PRONTO", 35, self.startx, self.starty)
        self.draw_text("COMO JOGAR", 35, self.instructionsx, self.instructionsy)
        self.draw_text("SOBRE", 35, self.creditsx, self.creditsy)
        self.draw_cursor()

    def update(self, dt, events):
        self.reset_keys()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True 
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

        self.move_cursor()
        self.check_input()
        self.background.update(dt)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface,text_rect)

    def move_cursor(self):
        if self.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.instructionsx + self.offset , self.instructionsy)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = 'Instructions'

    def check_input(self):
        self.move_cursor()
        if self.START_KEY:
            if self.state == 'Start':
                self.emit("CHOOSE_SHIP")
            elif self.state == 'Instructions':
                self.emit("INSTRUCTIONS")
            elif self.state == 'Credits':
                self.emit("CREDITS")
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
  
class InstructionsScene(MenuScene):
    def __init__(self, screen):
        MenuScene.__init__(self, screen)
        self.background = Background(self.screen)
        self.width, self.height = self.screen.get_size()
        self.mid_w, self.mid_h = self.width/2, self.height/2
        self.image = pygame.transform.scale(sprites.instructions, (970, 500))

    def check_input(self):
        self.move_cursor()
        if self.START_KEY:
            self.emit("CHOOSE_SHIP")
        if self.BACK_KEY:
            self.emit("RESTART")
           

    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))

        self.draw_text('COMO JOGAR', 35, self.mid_w, self.mid_h - 260)
        self.screen.blit(self.image, (self.width - 985, self.height - 520))

    def update(self, dt, events):
        self.reset_keys()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

        self.check_input()
        self.background.update(dt)

  
class CreditsScene(MenuScene):
    def __init__(self, screen):
        MenuScene.__init__(self, screen)
        self.background = Background(self.screen)
        self.width, self.height = self.screen.get_size()
        self.mid_w, self.mid_h = self.width/2, self.height/2

    def check_input(self):
        self.move_cursor()
        if self.BACK_KEY:
            self.emit("RESTART")
           

    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))

        self.draw_text('DESENVOLVIDO POR', 35, self.mid_w, self.mid_h - 250)
        self.draw_text('Carlos Alberto de Souza Junior', 25, self.mid_w, self.mid_h - 100)
        self.draw_text('Juan Beliene de Araujo', 25, self.mid_w, self.mid_h - 60)
        self.draw_text('Lucas Westfal', 25, self.mid_w, self.mid_h - 20)
        self.draw_text('Nicole dos Santos de Souza', 25, self.mid_w, self.mid_h + 20)
        self.draw_text('Pedro Henrique de Souza', 25, self.mid_w, self.mid_h + 60)
        self.draw_text('Pressione Backspace para voltar', 15, self.mid_w, self.height - 20)

    def update(self, dt, events):
        self.reset_keys()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

        self.check_input()
        self.background.update(dt)

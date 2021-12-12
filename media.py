import pygame


class Media:
    def __init__(self, win):
        self.width = win.get_width()
        self.height = win.get_height()
        self.win = win 
        
        #self.fonts = {}
        self.font = pygame.font.SysFont("arial", 45)
        self.colour = (255, 255, 255)
                
        
    def write(self, text, y):        
        '''
        size = 
        if str(size) in self.fonts:
            font = self.fonts[size]
        else:
            font = pygame.font.SysFont("arial", size)
            self.fonts[size] = font'''
        
        obj = self.font.render(text, True, self.colour)
        surf = pygame.Surface(obj.get_size())
        surf.fill((0, 0, 0))
        surf.set_alpha(128)
        
        pos = (self.width/2 - surf.get_width()/2, self.height * y - surf.get_height()/2)
        self.win.blit(surf, pos)
        self.win.blit(obj, pos)
        
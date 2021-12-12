import pygame


class Button:
    def __init__(self, x, y, w, h, text, center=None):
        self.rect = pygame.Rect(x, y, w, h)
        if center != None:
            self.rect.x = center.x + center.w/2 - w/2
            
        self.text = text 
        self.font = pygame.font.SysFont("arial", 30)
        self.textobj = self.font.render(self.text, True, (255, 255, 255))
        
        self.click = False 
        self.colour = (0, 0, 0)
        
    def update(self, events):
        self.click = False 
        
        if self.rect.collidepoint(events.mouse):
            self.colour = (165, 42, 42)
            if events.click:
                self.click = True
        else:
            self.colour = (0, 0, 0)
        
    def draw(self, win):
        self.rounded_rect(win, self.colour, self.rect, 40)
        win.blit(self.textobj, (self.rect.x + self.rect.w/2 - self.textobj.get_width()/2, self.rect.y + self.rect.h/2 - self.textobj.get_height()/2))
        
    def rounded_rect(self, surface, colour, rect, rad):
        x, y, w, h = rect 
        r = rad
        
        pygame.draw.ellipse(surface, colour, (x, y, r, r))
        pygame.draw.ellipse(surface, colour, (x + w - r, y, r, r))
        pygame.draw.ellipse(surface, colour, (x, y + h - r, r, r))
        pygame.draw.ellipse(surface, colour, (x + w - r, y + h - r, r, r))

        pygame.draw.rect(surface, colour, (x + r/2, y, w - r, r))
        pygame.draw.rect(surface, colour, (x + r/2,y + h - r/2 - r/2, w - r , r))
        pygame.draw.rect(surface, colour, (x, y + r/2, r, h - r))
        pygame.draw.rect(surface, colour, (x + w - r, y + r/2, r, h - r))

        pygame.draw.rect(surface, colour, (x + r/2, y + r/2, w - r, h - r))
        
        
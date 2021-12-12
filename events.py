import pygame


class Events:
    def __init__(self):
        self.update()
        
    def update(self):
        self.quit = False
        self.click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                
        self.mouse = pygame.mouse.get_pos()
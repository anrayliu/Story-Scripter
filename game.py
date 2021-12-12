import pygame
import events, media, button
import os #listdir, exists
import sys #exit
pygame.init()

class Game:
    def __init__(self, instructions):
        self.win = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Story Scripter")
        if os.path.exists("icon.png"):
            pygame.display.set_icon(pygame.image.load("icon.png"))
        
        self.backgrounds = {}
        self.instructions = instructions
        
        self.index = -1 #current index in instructions list
        self.background = None
        self.text = ""
        self.texty = 0.8
        self.buttons = []
        
        half = self.win.get_width()/2 #rects to center buttons 
        third = self.win.get_width()/3
        quarter = self.win.get_width()/4
        
        self.button_rects = {"1":[pygame.Rect(0, 0, self.win.get_width(), 0)],
                             "2":[pygame.Rect(0, 0, half, 0), pygame.Rect(half, 0, half, 0)],
                             "3":[pygame.Rect(0, 0, third, 0), pygame.Rect(third, 0, third, 0), pygame.Rect(third * 2, 0, third, 0)],
                             "4":[pygame.Rect(0, 0, quarter, 0), pygame.Rect(quarter, 0, quarter, 0), pygame.Rect(quarter * 2, 0, quarter, 0), pygame.Rect(quarter * 3, 0, quarter, 0)]}
        
        self.clock = pygame.time.Clock()
        self.events = events.Events()
        self.media = media.Media(self.win)
        
        self.load_images()
        self.next_instruction()
        
    def update(self):
        if self.buttons == []:
            if self.events.click:
                self.next_instruction()
        else:
            for number, i in enumerate(self.buttons):
                i.update(self.events)
                if i.click:
                    if i.text == self.instructions[self.index + 1][1]:
                        self.next_instruction()
                    else:
                        del self.buttons[number]
                        
    def next_instruction(self):
        if self.index < len(self.instructions) - 1:
            self.index += 1
            instruction = self.instructions[self.index]
            
            if instruction[0] == "options":
                self.buttons = []
                options = instruction[1].split(" ")
                for number, option in enumerate(options):
                    self.buttons.append(button.Button(0, self.win.get_height() * 0.7 , 200, 100, option, self.button_rects[str(len(options))][number]))
                self.texty = 0.6
                
            elif instruction[0] == "text":
                self.text = instruction[1]
                if self.index + 1 < len(self.instructions) -1:
                    if self.instructions[self.index + 1][0] == "options":
                        self.next_instruction()
                            
            elif instruction[0] == "background":
                self.background = self.backgrounds[instruction[1]]
                self.next_instruction()
                
            elif instruction == "empty":
                self.next_instruction()
            
            elif instruction[0] == "answer":
                self.buttons = []
                self.texty = 0.8
                self.next_instruction()
                
            elif instruction[0] == "comment":
                self.next_instruction()
                            
    def draw(self):
        self.win.fill((0, 0, 0))
        
        if not self.background == None:
            self.win.blit(self.background, (0, 0))
        
        if len(self.text) > 60:
            seperator = self.get_seperator()
            self.media.write(self.text[:seperator], self.texty - 0.05)
            self.media.write(self.text[seperator + 1:], self.texty + 0.05)
        else:
            self.media.write(self.text, self.texty)
        
        for i in self.buttons:
            i.draw(self.win)
            
    def get_seperator(self):
        seperator = 60
        while self.text[seperator] != " ":
            seperator -= 1
            if seperator < 0:
                return 0
        return seperator
                        
    def load_images(self):
        for image in os.listdir("assets"):
            if image[-4:] == ".png" or image[-4:] == ".jpg":
                self.backgrounds[image] = pygame.transform.scale(pygame.image.load("assets\\" + image), self.win.get_size())
        
    def run(self):
        while True:
            self.clock.tick(60)
            
            self.events.update()
            if self.events.quit:
                pygame.quit()
                sys.exit()
            self.update()
            self.draw()
            
            pygame.display.update()

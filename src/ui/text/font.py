import pygame

class Font:
    def __init__(self, context, glyph, grid_size):
        self.context = context 
        self.glyph = glyph 
        self.grid_size = grid_size

    def render_caracter(self, caracter):
        id = ord(caracter) - 32
        image = self.context.assets[self.glyph]
        cols = image.width // self.grid_size[0] 
        x = id % cols 
        y = id // cols 
        return self.context.assets[f"{self.glyph}.{x}.{y}"]
    
    def render_text(self, text):
        image = pygame.Surface((self.grid_size[0] * len(text), self.grid_size[1]), pygame.HWSURFACE | pygame.SRCALPHA)
        for i in range(len(text)):
            image.blit(self.render_caracter(text[i]), (self.grid_size[0] * i, 0))   
        return image      
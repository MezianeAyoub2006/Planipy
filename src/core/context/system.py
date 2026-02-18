import pygame 
import src.core as core


class System:
    def __init__(self, context : core.Context):
        self.context = context 
        
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.context.quit()
    
    
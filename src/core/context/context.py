import pygame
import sys 

import src.core as core


class Context:
    system : core.System
    runtime : core.Runtime 
    event_bus : core.EventBus 
    
    def __init__(self, resolution):
        self.runtime = core.Runtime(self, resolution, pygame.RESIZABLE) 
        self.event_bus = core.EventBus(self) 
        self.system = core.System(self) 

    def run(self):
        self.runtime.run()

    def quit(self):
        pygame.quit()
        sys.exit()

    @property
    def keyboard_active(self):
        return pygame.key.get_pressed() 

    @property 
    def keyboard_pressed(self):
        return pygame.key.get_just_pressed() 
    
    @property 
    def keyboard_released(self):
        return pygame.key.get_just_released()
    
    @property 
    def dt(self):
        return self.runtime.dt 
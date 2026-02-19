import pygame
import sys 

import src.core as core


class Context:
    system : core.System
    runtime : core.Runtime 
    event_bus : core.EventBus 
    root : core.Node 
    renderer : core.Renderer
    
    def __init__(self, resolution):
        self.runtime = core.Runtime(self, resolution, pygame.RESIZABLE) 
        self.event_bus = core.EventBus(self) 
        self.system = core.System(self) 
        self.root = core.Node(self)
        self.renderer = core.Renderer(self)

    def run(self):
        self.runtime.run()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self, element, **kwargs):
        self.renderer.draw(element, **kwargs) 

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
    
    @property 
    def screen(self):
        return self.runtime.screen
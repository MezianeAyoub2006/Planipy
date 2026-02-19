import pygame 
import time 
import ctypes
import src.core as core

class Runtime:
    def __init__(self, context : core.Context, resolution, flags):
        self._diseable_dpi()
        self.context = context 
        self.screen = pygame.display.set_mode(resolution, flags) 
        self.clock = pygame.time.Clock()
        self.latest_time = time.perf_counter()
        pygame.display.set_icon(pygame.image.load("assets/images/logo.png"))
        pygame.display.set_caption("Planipy")
        self.dt = 1

    def _diseable_dpi(self):
        try:
            ctypes.windll.user32.SetProcessDPIAware() 
        except:
            pass

    def _delta_time(self):
        self.dt = time.perf_counter() - self.latest_time 
        self.latest_time = time.perf_counter()

    def run(self):
        while True:
            self._delta_time()
            self.context.system.poll_events()
            self.context.root.update_all()
            pygame.display.flip()
            self.clock.tick(1000)
            self.context.event_bus.clear()
            self.context.renderer.tasks.clear()
            


    
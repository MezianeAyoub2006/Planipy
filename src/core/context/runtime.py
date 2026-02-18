import pygame 
import time 
import src.core as core

class Runtime:
    def __init__(self, context : core.Context, resolution, flags):
        self.context = context 
        self.screen = pygame.display.set_mode(resolution, flags) 
        self.clock = pygame.time.Clock()
        self.latest_time = time.perf_counter()
        self.dt = 1

    def _delta_time(self):
        self.dt = time.perf_counter() - self.latest_time 
        self.latest_time = time.perf_counter()

    def run(self):
        while True:
            self._delta_time()
            self.context.system.poll_events()
            pygame.display.flip()
            self.clock.tick(1000)
            self.context.event_bus.clear()
            


    
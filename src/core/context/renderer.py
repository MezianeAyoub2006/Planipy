import pygame
import src.core as core 

from operator import itemgetter


class Renderer:
    def __init__(self, context):
        self.context = context 
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task) 

    def update(self):
        for task in sorted(self.tasks, key = itemgetter("order")):
            self.handle_task(task)

    def handle_task(self, task):
        if task["type"] == "surface":
            self.context.screen.blit(task["content"], task["position"]) 
        elif task["type"] == "rect":
            pygame.draw.rect(self.context.screen, task["color"], task["content"])
        else:
            raise core.CoreException(f"Unknown task type \"{task["type"]}\"")

    def draw(self, element, **kwargs):
        task = {"order" : kwargs.get("order", 0)}
        if isinstance(element, str):
            self.draw(self.context.assets[element], **kwargs)
            return 
        elif isinstance(element, pygame.Rect):
            task["type"] = "rect"
            task["color"] = kwargs.get("color", core.RED)
        elif isinstance(element, pygame.Surface):
            task["type"] = "surface"
            task["position"] = kwargs.get("position", (0, 0))
        else:
            raise core.CoreException(f"Wrong rendering object type \"{element.__class__.__name__}\"")
        task["content"] = element
        self.handle_task(task)
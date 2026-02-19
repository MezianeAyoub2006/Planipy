import src.core as core 
import pygame 


class Test(core.Node):
    def __init__(self, context):
        core.Node.__init__(self, context)
        self.asset = pygame.image.load("assets/images/glyphs/main.png").convert_alpha()
    def update(self):
        self.context.draw(self.asset)

context = core.Context((500, 500)) 
context.root.attach(Test(context))
context.run()
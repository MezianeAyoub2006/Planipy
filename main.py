import src.core as core 
import pygame 


class Test(core.Node):
    def __init__(self, context):
        core.Node.__init__(self, context)
        self.context.load_image("test", "assets/images/glyphs/main.png")
        self.context.load_spritesheet("glyph", "assets/images/glyphs/main.png", (24, 24))
    def update(self):
        for x in range(5):
            for y in range(3):
                self.context.draw(f"glyph.{x}.{y}", position = (x * 24, y * 24))

context = core.Context((500, 500)) 
context.root.attach(Test(context))
context.run()
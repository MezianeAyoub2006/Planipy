import src.core as core 
import src.ui as ui
import pygame 


class Test(core.Node):
    def __init__(self, context):
        core.Node.__init__(self, context)
        self.context.load_spritesheet("glyph", "assets/images/glyphs/main.png", (24, 28))
        self.font = ui.Font(self.context, "glyph", (24, 28))

    def update(self):
        img = self.font.render_text("typedef struct {char* name; int age} Human;")
        self.context.draw(img)
        self.context.draw(img, position = (0, 28))

context = core.Context((500, 500)) 
context.root.attach(Test(context))
context.run()
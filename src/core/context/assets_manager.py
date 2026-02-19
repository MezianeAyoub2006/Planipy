import pygame
import src.core as core 


class AssetsManager:
    def __init__(self, context):
        self.context = context 
        self.assets = {}

    def _load_image(self, path, scale = (1, 1)):
        original_image = pygame.image.load(path).convert_alpha()
        if scale != (1, 1):
            width = original_image.get_width()
            height = original_image.get_height()
            scaled_image = pygame.transform.scale(
                original_image, (
                    scale[0] * width,
                    scale[1] * height
                )
            )
            return scaled_image
        return original_image 

    def load_image(self, path, name, scale = (1, 1)):
        self.assets[name] = self._load_image(path, scale) 

    def load_spritesheet(self, path, name, tile_size, scale = (1, 1)):
        spritesheet_image = self._load_image(path, scale) 
        width = spritesheet_image.get_width()
        height = spritesheet_image.get_height()
        final_tile_size = (
            scale[0] * tile_size[0],
            scale[1] * tile_size[1] 
        )
        for x in range(int(width // final_tile_size[0])):
            for y in range(int(height // final_tile_size[1])):
                self.assets[f"{name}.{x}.{y}"] = spritesheet_image.subsurface((
                    x * final_tile_size[0],
                    y * final_tile_size[1],
                    final_tile_size[0],
                    final_tile_size[1]
                )).copy()  
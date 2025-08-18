from os import walk
from os.path import join
import pygame

def import_folder(*path, alpha = True, format='.png'):
    surface_list = []
    
    for folder_name, sub_folder, img_files in walk(*path):
        for image in img_files:
            full_path = join(*path, image)
            image_surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
            surface_list.append(image_surf)
    
    
    return surface_list

def import_sprite_sheet(*path, cols, rows):
    full_path = join(*path) + f'{format}'
    sprites = {status: [] for status in ['up', 'down', 'left', 'right']}
    
    for col in range(cols):
        for row in range(rows):
            sprite_sheet = import_folder(full_path, alpha=True)
            col_width = sprite_sheet.get_width() // cols
            row_height = sprite_sheet.get_height() // rows
            rect = pygame.Rect(col * col_width, row * row_height, col_width, row_height)
            image = pygame.Surface(rect.size, pygame.SRCALPHA)

            #sprite_sheet = pygame.image.load(full_path).convert_alpha()

            #rect = pygame.Rect(i, j, size[0], size[1])
            #image = pygame.Surface(rect.size, pygame.SRCALPHA)
            #image.blit(sprite_sheet, (0, 0), rect)
            #sprites.append(image)
    
    return sprites

from os import walk
from os.path import join
import pygame

def import_folder(*path):
    surface_list = []
    
    for folder_name, sub_folder, img_files in walk(*path):
        for image in img_files:
            full_path = join(*path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    
    
    return surface_list

#def import_sprite_sheet(*path, cols, rows, format='.png'):
    full_path = join(*path) + f'{format}'
    sprites = {}
    
    for i in range(0, sprite_sheet.get_width(), size[0]):
        for j in range(0, sprite_sheet.get_height(), size[1]):
            sprite_sheet = pygame.image.load(full_path).convert_alpha()
            #rect = pygame.Rect(i, j, size[0], size[1])
            #image = pygame.Surface(rect.size, pygame.SRCALPHA)
            #image.blit(sprite_sheet, (0, 0), rect)
            #sprites.append(image)
    
    return sprites

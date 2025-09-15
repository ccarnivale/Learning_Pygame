from os import walk
from os.path import join
import pygame

def import_image(*path, alpha = True):
    full_path = join(*path)
    image_surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
    return image_surf


def import_folder(*path, alpha = True):
    surface_list = []
    
    for folder_name, sub_folder, img_files in walk(join(*path)):
        for image in img_files:
            full_path = join(*path, image)
            #print(full_path)
            image_surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
            surface_list.append(image_surf)
    
    
    return surface_list

def import_tilemap(*path, cols, rows, alpha = True):
    full_path = join(*path)
    tilemap = import_image(full_path, alpha=alpha)
    tile_width = tilemap.get_width() // cols
    tile_height = tilemap.get_height() // rows
    tiles = {}
    
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * tile_width, row * tile_height, tile_width, tile_height)
            image_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
            image_surf.blit(tilemap, (0, 0), rect)
            tiles[(row, col)] = image_surf
    
    return tiles

def import_sprite_sheet(*path, cols, rows, names: list, alpha = True):
    full_path = join(*path)
    sprites = {}
    grouped = {name: [] for name in names}
    sprite_sheet = import_image(full_path, alpha=alpha)
    col_width = sprite_sheet.get_width() // cols
    row_height = sprite_sheet.get_height() // rows
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * col_width, row * row_height, col_width, row_height)
            image_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
            
            image_surf.blit(sprite_sheet, (0, 0), rect)
            sprites[(row, col)] = image_surf 

            #sprite_sheet = pygame.image.load(full_path).convert_alpha()
    #return sprites
    for (row, col), image in sprites.items():
        grouped[names[row]].append(image)
    return grouped  

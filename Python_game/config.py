animations = {'up': [], 'down':[], 'left': [], 'right': []}
        
for animation in animations.keys():
    full_path = "C:\\Users\\Chris Carnivale\\OneDrive\\Desktop\\Python_fun_project\\Python_game\\Assets\\Sprout Lands - Sprites - Basic pack\\Sprout Lands - Sprites - Basic pack\\Characters\\" + animation 
    animations[animation] = import_folder(full_path)
    
    
def import_folder(path):
    surface_list = []
    
    for folder in walk(path):
        print(folder)
    
    
    return surface_list


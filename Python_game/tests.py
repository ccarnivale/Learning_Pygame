import os
from os.path import join

##for folder in os.listdir("C:\\Users\\Chris Carnivale\\OneDrive\\Desktop\\Python_fun_project\\First-Python-Game\\Python_game\\Assets\\Sprout Lands Sprites\\Sprout Lands - Sprites - Basic pack\\Characters\\"):
#        print(folder)

#for folder in os.listdir("C:\\Users\\Chris Carnivale\\OneDrive\\Desktop\\Python_fun_project\\Python_game\\Assets\\Sprout Lands Sprites \\Sprout Lands - Sprites - Basic pack\\Characters\\"):
#        print(folder)

print(os.getcwd())
path = os.getcwd()
print('test')
animations = {'up': [], 'down':[], 'left': [], 'right': []}
print(list(animations.keys())[1])
print(os.path.join('Python_game','Assets','Sprout Lands Sprites','Sprout Lands - Sprites - Basic pack','Characters', list(animations.keys())[1]))
"""
This is the main file that will be executed to run the game

Users should be able to launch the game using python ./main.py when in the folder to launch game
"""
import pygame

#Some notes: It will be easier to think of the game as cells which are groups of pixels for movement reasons 
CELL_SIZE = 20
GAME_SPEED = 10 #TODO: Modify later with custom settings to have game speed change



class Python:
    """
    So for our python right now we need to consider some things for movement and gameplay
    1. the position of our player on the board using x and y
    2. The size of our python (Later we will need to address length)
    3. the direction of our character. with drawing direcition we have +/- x and +/- y to do n,s,w,e
    4. Just a color of our character that we will draw  
    """
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.direction = (1,0)
        self.color = (0, 200, 0)

    """
    What are some functions needed for the game / pygame?
    1. We will need a function to handle moving the character using pygame event handles
    2. We will need a function to draw the character for pygame reasons
    3. We will need a function to modify the x and y using direction and game speed
    """

    def key_movement(self,key):
        #Can use a dictionary to store the key event and the direction associated with it
        directions_map = {
            pygame.K_UP: (0,-1),
            pygame.K_DOWN: (0,1),
            pygame.K_LEFT: (-1,0),
            pygame.K_RIGHT: (1,0)
        }

        #Then we can check if the key press is in the dictionary to then modify the python's direction
        if key in directions_map:
            self.direction = directions_map[key]

class Target:
    def __init__(self):
        pass


if __name__ == "__main__":
    #Basic Init for pygame
    pygame.init()
    pygame.display.set_caption("Python Python Game")


    #Screen Setup
    default_res = (800,600)
    screen = pygame.display.set_mode(default_res)

    clock = pygame.time.Clock()


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #TODO: Maybe here later I can have inital game setup for screen on first loop

        
    
    pygame.quit()


    
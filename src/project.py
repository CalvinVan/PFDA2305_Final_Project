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


    
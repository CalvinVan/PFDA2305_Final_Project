"""
This is the main file that will be executed to run the game

Users should be able to launch the game using python ./main.py when in the folder to launch game
"""
import pygame

class Python:
    def __init__(self):
        pass

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

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #TODO: Maybe here later I can have inital game setup for screen on first loop

        
    
    pygame.quit()


    
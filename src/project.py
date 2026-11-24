"""
This is the main file that will be executed to run the game

Users should be able to launch the game using python ./main.py when in the folder to launch game
"""
import pygame
import random

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

    #Function for updating the x and y based on our direction property
    def move(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy

    def draw(self, surface):
        #get size of character
        rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)

class Target:
    """
    Some notes:
    A target will need an x,y position, size (cell), color, and where it can spawn (if we are using cells that means you can image there are rows and columns)
    
    As for functions, for now we will handle respawn and drawing it 
    """
    def __init__(self, size, cols, rows):
        self.size = size
        self.x = 0 #So for x and y, this will basically be determined by which row and column it is if we imagine the game to be a grid
        self.y = 0
        self.rows = rows
        self.cols = cols
        self.color = (200,0,0)

    def respawn(self, player): #here targets will respawn at a random location that is not == to where the player is
        while True:
            x = random.randint(0, self.cols- 1)
            y = random.randint(0, self.rows - 1)
            if (x,y) != (player.x, player.y):
                self.x, self.y = x,y
                return
            #so if it is == we will pick a new x and y to position it
    
    def draw(self, surface): #TODO at some point we want to import an asset to use instead of using a rectangle
        rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)
    


if __name__ == "__main__":
    #Basic Init for pygame
    pygame.init()
    pygame.display.set_caption("Python Python Game")


    #Screen Setup
    default_res = (800,600)
    screen = pygame.display.set_mode(default_res)

    clock = pygame.time.Clock()

    #Now here we will make screen a grid
    grid_cols = default_res[0] // CELL_SIZE
    grid_rows = default_res[1] // CELL_SIZE

    #spawn position start in middle
    player = Python(x = grid_cols // 2,
                    y = grid_rows // 2,
                    size = CELL_SIZE)

    #place our first target before looping

    target = Target(CELL_SIZE, grid_cols, grid_rows)
    target.respawn(player)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: #check for keypress
                player.key_movement(event.key)

        #Update the player position
        player.move()


        #check for when a player and target match x and y and need to remove
        if (player.x, player.y) == (target.x, target.y):
            target.respawn(player)
    

        #Now draw it based on the now updated movement
        #eventually we want a clock update for later
        screen.fill((0,0,0)) 
        target.draw(screen) #draw target on screen too
        player.draw(screen) #draw player on the screen surface
        pygame.display.flip() #show the new screen drawn behind scene

        clock.tick(GAME_SPEED)

        #TODO: Maybe here later I can have inital game setup for screen on first loop

        
    
    pygame.quit()


    
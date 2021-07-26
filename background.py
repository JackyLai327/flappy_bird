import pygame

class Background: 
    def __init__(self):
        self.screen = pygame.display.set_mode((350, 700)) #create a screen (width, height)
        self.clock = pygame.time.Clock() #use Clock to define FPS
        self.bg = pygame.image.load("assets/sprites/background-day.png").convert() #converts the image
        self.bg = pygame.transform.scale(self.bg, (350, 700)) #double the size 
        self.floor = pygame.image.load("assets/sprites/base.png").convert()
        self.floor = pygame.transform.scale(self.floor, (350, 100))
        self.floor_x_position = 0

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_position, 630))
        self.screen.blit(self.floor, (self.floor_x_position + 350, 630)) #a new floor outside the screen on the right
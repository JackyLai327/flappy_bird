import pygame

class Bird:
    def __init__(self):
        self.bird_downflap = pygame.image.load("assets/sprites/bluebird-downflap.png").convert_alpha()
        self.bird_midflap = pygame.image.load("assets/sprites/bluebird-midflap.png").convert_alpha()
        self.bird_upflap = pygame.image.load("assets/sprites/bluebird-upflap.png").convert_alpha()
        self.bird_frames = [self.bird_downflap, self.bird_midflap, self.bird_upflap, self.bird_midflap] #create animation 
        self.bird_index = 0
        self.bird = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (75, 250)) #create a rectangle around the bird
        self.gravity = 0.2
        self.bird_movement = 0
        self.BIRDFLAP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.BIRDFLAP, 200)


    def rotate_bird(self, b):
        new_bird = pygame.transform.rotozoom(b, -self.bird_movement * 4, 1)
        return new_bird

    def bird_animation(self):
        new_bird = self.bird_frames[self.bird_index]
        new_bird_rect = new_bird.get_rect(center = (75, self.bird_rect.centery))
        return (new_bird, new_bird_rect)

    
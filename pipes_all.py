import pygame, random, background

class Pipes:
    def __init__(self):
        self.pipe = pygame.image.load("assets/sprites/pipe-green.png").convert()
        self.pipe_list = [] #throw in a lot of rectangles
        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1000)
        self.pipe_height = [350, 370, 385, 400, 435, 450, 470]
        self.screen = background.Background().screen

    def create_pipe(self):
        random_pipe_position = random.choice(self.pipe_height)
        bottom_pipe = self.pipe.get_rect(midtop = (700, random_pipe_position))
        top_pipe = self.pipe.get_rect(midbottom = (700, random_pipe_position - 150))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for p in pipes:
            p.centerx -= 2.5
        return pipes

    def draw_pipes(self, pipes):
        for p in pipes:
            if p.bottom >= 600:
                self.screen.blit(self.pipe, p)
            else: 
                flip_pipe = pygame.transform.flip(self.pipe, False, True)
                self.screen.blit(flip_pipe, p)
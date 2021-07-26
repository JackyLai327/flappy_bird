import pygame
pygame.mixer.pre_init()

class Sounds: 
    def __init__(self):
        self.flap_sound = pygame.mixer.Sound("assets/sounds/sfx_wing.wav")
        self.death_sound = pygame.mixer.Sound("assets/sounds/sfx_hit.wav")
        self.score_sound = pygame.mixer.Sound("assets/sounds/sfx_point.wav")
        self.score_sound_countdown = 1000

    def play_flap_sound(self):
        self.flap_sound.play()

    def play_collision_sound(self):
        self.death_sound.play()

    def play_score_sound(self):
        self.score_sound.play()
        self.score_sound_countdown = 1000
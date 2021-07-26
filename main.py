import pygame
from game import Game

def main():
    pygame.mixer.pre_init() #so the sounds don't delay 
    pygame.init() 
    game = Game()
    game.game_loop()

if __name__ == "__main__":
    main()
import pygame, background

class Score:
    def __init__(self):
        self.screen = background.Background().screen
        self.game_font = pygame.font.Font("04B_19.ttf", 40)
        self.score = -.99
        self.high_score = 0


    def score_display(self, game_state):
        if game_state == "main_game":
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = (175, 75))
            self.screen.blit(score_surface, score_rect)
        if game_state == "game_over":
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = (175, 75))
            self.screen.blit(score_surface, score_rect)

            highscore_surface = self.game_font.render("highest: " + str(int(self.high_score)), True, (255, 255, 255))
            highscore_rect = score_surface.get_rect(center = (80, 150))
            self.screen.blit(highscore_surface, highscore_rect)
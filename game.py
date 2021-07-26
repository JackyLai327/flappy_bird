import sys, pygame, sounds, background, bird_sprite, pipes_all, score

class Game: 
    def __init__(self):
        self.sounds = sounds.Sounds()
        self.game_active = False
        self.screen = background.Background().screen
        self.bird = bird_sprite.Bird()
        self.pipes = pipes_all.Pipes()
        self.scores = score.Score()
        self.background = background.Background()
        self.game_over = pygame.image.load("assets/sprites/message.png").convert_alpha()
        self.game_over_rect = self.game_over.get_rect(center = (175, 350))

    def check_collision(self, pipes):
        if self.bird.bird_rect.bottom >= 600 or self.bird.bird_rect.top <= 0:
            self.sounds.death_sound.play()
            return False
        
        for p in pipes: 
            if self.bird.bird_rect.colliderect(p):
                self.sounds.death_sound.play()
                return False

        return True

    def game_loop(self):
        while True: 
            for event in pygame.event.get(): #captures all the events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE and self.game_active:
                        self.bird.bird_movement = -5
                        self.sounds.flap_sound.play()
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.pipes.pipe_list.clear()
                        self.bird.bird_rect.center = (75, 250)
                        self.bird.bird_movement = 0
                        self.scores.score = -1
                if event.type == self.pipes.SPAWNPIPE:
                    self.pipes.pipe_list.extend(self.pipes.create_pipe())
                if event.type == self.bird.BIRDFLAP:
                    if self.bird.bird_index < 2:
                        self.bird.bird_index += 1
                    else:
                        self.bird.bird_index = 0

                    self.bird.bird, self.bird.bird_rect = self.bird.bird_animation()

            self.screen.blit(self.background.bg, (0, 0)) #put 1 surface on another

            if self.game_active:
                #bird
                self.bird.bird_movement += self.bird.gravity
                rotated_bird = self.bird.rotate_bird(self.bird.bird)
                self.bird.bird_rect.centery += self.bird.bird_movement #move the bird rectangle down
                self.screen.blit(rotated_bird, self.bird.bird_rect)
                self.game_active = self.check_collision(self.pipes.pipe_list)

                #pipe
                self.pipes.pipe_list = self.pipes.move_pipes(self.pipes.pipe_list)
                self.pipes.draw_pipes(self.pipes.pipe_list)

                self.scores.score += 0.008
                self.sounds.score_sound_countdown -= 8
                if self.scores.score > 0.99 and self.sounds.score_sound_countdown <= 8: 
                    self.sounds.score_sound.play()
                    self.sounds.score_sound_countdown = 1000
                if self.scores.score > self.scores.high_score: self.scores.high_score = self.scores.score
                self.scores.score_display("main_game")
            else: 
                self.screen.blit(self.game_over, self.game_over_rect)
                self.scores.score_display("game_over")

            #floor
            self.background.floor_x_position -= 1 #floor moving to the right
            self.background.draw_floor()
            if self.background.floor_x_position <= -350:
                self.background.floor_x_position = 0

            pygame.display.update() #draws everything before this line
            self.background.clock.tick(120) #120 FPS
            
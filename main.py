import pygame, sys, random

def draw_floor():
    screen.blit(floor, (floor_x_position, 630))
    screen.blit(floor, (floor_x_position + 350, 630)) #a new floor outside the screen on the right

def create_pipe():
    random_pipe_position = random.choice(pipe_height)
    bottom_pipe = pipe.get_rect(midtop = (700, random_pipe_position))
    top_pipe = pipe.get_rect(midbottom = (700, random_pipe_position - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for p in pipes:
        if p.bottom >= 600:
            screen.blit(pipe, p)
        else: 
            flip_pipe = pygame.transform.flip(pipe, False, True)
            screen.blit(flip_pipe, p)

def check_collision(pipes):
    if bird_rect.bottom >= 600 or bird_rect.top <= 0:
        death_sound.play()
        return False
    
    for p in pipes: 
        if bird_rect.colliderect(p):
            death_sound.play()
            return False

    return True

def rotate_bird(b):
    new_bird = pygame.transform.rotozoom(b, -bird_movement * 4, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (75, bird_rect.centery))
    return (new_bird, new_bird_rect)

def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (175, 75))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (175, 75))
        screen.blit(score_surface, score_rect)

        highscore_surface = game_font.render("highest: " + str(int(high_score)), True, (255, 255, 255))
        highscore_rect = score_surface.get_rect(center = (80, 150))
        screen.blit(highscore_surface, highscore_rect)

pygame.mixer.pre_init() #so the sounds don't delay 
pygame.init() 
screen = pygame.display.set_mode((350, 700)) #create a screen (width, height)
clock = pygame.time.Clock() #use Clock to define FPS
game_font = pygame.font.Font("04B_19.ttf", 40)

# Game Variables
gravity = 0.2
bird_movement = 0
game_active = False
score = -.99
high_score = 0

bg = pygame.image.load("assets/sprites/background-day.png").convert() #converts the image
bg = pygame.transform.scale(bg, (350, 700)) #double the size 

floor = pygame.image.load("assets/sprites/base.png").convert()
floor = pygame.transform.scale(floor, (350, 100))
floor_x_position = 0

bird_downflap = pygame.image.load("assets/sprites/bluebird-downflap.png").convert_alpha()
bird_midflap = pygame.image.load("assets/sprites/bluebird-midflap.png").convert_alpha()
bird_upflap = pygame.image.load("assets/sprites/bluebird-upflap.png").convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap, bird_midflap] #create animation 
bird_index = 0
bird = bird_frames[bird_index]
bird_rect = bird.get_rect(center = (75, 250)) #create a rectangle around the bird


BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

pipe = pygame.image.load("assets/sprites/pipe-green.png").convert()
pipe_list = [] #throw in a lot of rectangles
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1000)
pipe_height = [350, 370, 385, 400, 435, 450, 470]

game_over = pygame.image.load("assets/sprites/message.png").convert_alpha()
game_over_rect = game_over.get_rect(center = (175, 350))

flap_sound = pygame.mixer.Sound("assets/sounds/sfx_wing.wav")
death_sound = pygame.mixer.Sound("assets/sounds/sfx_hit.wav")
score_sound = pygame.mixer.Sound("assets/sounds/sfx_point.wav")
score_sound_countdown = 1000

while True: 
    for event in pygame.event.get(): #captures all the events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -5
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (75, 250)
                bird_movement = 0
                score = -1
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird, bird_rect = bird_animation()

    screen.blit(bg, (0, 0)) #put 1 surface on another

    if game_active:
        #bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement #move the bird rectangle down
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        #pipe
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score += 0.008
        score_sound_countdown -= 8
        if score > 0.99 and score_sound_countdown <= 8: 
            score_sound.play()
            score_sound_countdown = 1000
        if score > high_score: high_score = score
        score_display("main_game")
    else: 
        screen.blit(game_over, game_over_rect)
        score_display("game_over")

    #floor
    floor_x_position -= 1 #floor moving to the right
    draw_floor()
    if floor_x_position <= -350:
        floor_x_position = 0

    pygame.display.update() #draws everything before this line
    clock.tick(120) #120 FPS
    
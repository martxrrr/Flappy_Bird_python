import pygame
import random

WIDTH, HEIGHT = 900, 600
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LIST_LEN = 3
GROUND_BORDER = 115
BIRD = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bird1.png")
BIRD_WIDTH = BIRD.get_height()
BIRD_HEIGHT = BIRD.get_width()
BIRD_X, BIRD_Y = 100, 300
BIRD_VEL = 6
PIPE_VEL = 8
PIPE_POS_X = 960
PIPE_GAP = 70

BG = pygame.transform.scale(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bg.png"), (WIDTH, HEIGHT))
GROUND = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/ground.png")

PIPEDOWN = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png")
PIPEDOWN_MASK = pygame.mask.from_surface(PIPEDOWN)

PIPEUP = pygame.transform.rotate(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png"), 180)
PIPEUP_MASK = pygame.mask.from_surface(PIPEUP)


class Pipes:
    def __init__(self):
        #pipedown
        self.down_x = PIPE_POS_X
        self.down_y = random.randint(145, 465)

        #pipeup
        self.up_x = PIPE_POS_X
        self.up_y = (self.down_y - PIPEUP.get_height()) - PIPE_GAP

    def pipe_draw(self, screen):
        #pipedown
        screen.blit(PIPEDOWN, (self.down_x, self.down_y))
        screen.blit(PIPEUP, (self.up_x, self.up_y))

    def spawn(self):
        if self.down_x <= -60 or self.up_x <= -60: 
            self.down_x = PIPE_POS_X
            self.up_x = PIPE_POS_X
            self.down_y = random.randint(145, 465)
            self.up_y = (self.down_y - PIPEUP.get_height()) - PIPE_GAP       

    def move_pipe(self):
        self.down_x -= PIPE_VEL
        self.up_x -= PIPE_VEL
        self.spawn()

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bird_list = []
        self.bird_count = 0
        self.animation_speed = 0.1
        self.jump_count = 10

    def draw_bird(self, screen):
        for x in range(LIST_LEN):
            bird = pygame.image.load(f"PYTHON/Learning/Games/flappy_folder/flappy/bird{x + 1}.png")
            self.bird_list.append(bird)

        self.bird_count += self.animation_speed
        if self.bird_count > LIST_LEN: self.bird_count = 0
        screen.blit(self.bird_list[int(self.bird_count)], (self.x, self.y))


    def move(self, keys):
        self.y += BIRD_VEL

        if self.y >= HEIGHT - GROUND_BORDER: self.y = HEIGHT - GROUND_BORDER
        if self.y < 0: self.y = 0

        if keys[pygame.K_w]:
            self.y -= self.jump_count
    
def main():

    def draw_window(screen):
        screen.blit(BG, (0,0))
        screen.blit(GROUND, (0, HEIGHT - (GROUND.get_height() / 2)))

    running = True
    clock = pygame.time.Clock()
    bird = Bird(BIRD_X, BIRD_Y)
    obstacle = Pipes()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False  



        keys = pygame.key.get_pressed()

        draw_window(SCREEN)
        bird.draw_bird(SCREEN)
        bird.move(keys)

        obstacle.pipe_draw(SCREEN)
        obstacle.move_pipe()

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
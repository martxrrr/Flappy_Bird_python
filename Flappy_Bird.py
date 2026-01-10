import pygame
pygame.init()

import random

WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 60
BIRD_VEL = 4
OBST_VEL = 5
PIPE_SPACE = 90
PIPES_START_POS = 950


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("flappy/bird1.png").convert_alpha())

BG = pygame.transform.scale(pygame.image.load("flappy/bg.png"), (WIDTH, HEIGHT))
GROUND = pygame.image.load("flappy/ground.png").convert_alpha()
PIPEDOWN = pygame.image.load("flappy/pipedown.png").convert_alpha()
PIPEUP = pygame.transform.rotate(PIPEDOWN, 180)

class Obstacles():
    def __init__(self):
        #Bottom pipe
        self.x1 = PIPES_START_POS
        self.y1 = random.randint(173, 514)

        #Top pipe       
        self.y2 = (self.y1 - PIPE_SPACE) - PIPEDOWN.get_height() 
        self.x2 = PIPES_START_POS

    def draw(self, screen):
        screen.blit(PIPEUP, (self.x2, self.y2))
        screen.blit(PIPEDOWN, (self.x1, self.y1))

    def move(self, vel):
        self.x1 -= vel
        self.x2 -= vel

        if self.x1 < -70:
            self.x1 = 950
            self.spawn()

        if self.x2 < -70:
            self.x2 = 950
            self.spawn()

    def spawn(self):
        self.y1 = random.randint(123, 514)
        self.y2 = (self.y1 - PIPE_SPACE) - PIPEDOWN.get_height()



class Bird():
    bird_images = []
    bird_count = 0 
    animation_speed = 0.1 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.jump_count = 10

     
    def draw(self, screen):
        for x in range(3):
            self.bird_images.append(pygame.image.load(f"flappy/bird{x+1}.png").convert_alpha())

        self.bird_count += self.animation_speed
        curr_bird = self.bird_images[int(self.bird_count)]
        if self.bird_count >= len(self.bird_images): 
            curr_bird = 0

        screen.blit(curr_bird,(self.x, self.y))

    def jump(self):
        self.y -= self.jump_count

    def move(self, keys):
        self.y += BIRD_VEL
        if keys[pygame.K_w]:
            self.jump()

        if self.y <= 0: self.y = 0
        if self.y >= HEIGHT - 115: self.y = HEIGHT - 115

def main():
    clock = pygame.time.Clock()

    blit_images = [(BG, (0,0)), (GROUND, (0, 530))]
    bird = Bird(100, 300)
    obstacle = Obstacles()

    def draw_screen(screen, blit_images):
        for image in blit_images:
            screen.blit(*image)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        draw_screen(SCREEN, blit_images)
        bird.draw(SCREEN)
        bird.move(keys)

        obstacle.draw(SCREEN)
        obstacle.move(OBST_VEL)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
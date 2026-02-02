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
pygame.display.set_caption("PYTHON/Learning/Games/flappy_folder/Flappy Bird")
pygame.display.set_icon(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bird1.png").convert_alpha())

BG = pygame.transform.scale(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bg.png"), (WIDTH, HEIGHT))
GROUND = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/ground.png").convert_alpha()
PIPEDOWN = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png").convert_alpha()#bottom pipe
PIPEUP = pygame.transform.rotate(PIPEDOWN, 180)

SPAWN_EVENT = pygame.event.custom_type()
pygame.time.set_timer(SPAWN_EVENT, 2500)

#pygame.Rect(x, y, w, h) - it's like a container for an image

class Obstacles():
    obstacle_list = []
    obstacle_count = 3
    def __init__(self):
        #Bottom pipe
        self.pipedown_x = PIPES_START_POS
        self.pipedown_y = random.randint(173, 514)
        self.pipedown_width = PIPEDOWN.get_width()
        self.pipedown_height = PIPEDOWN.get_height()

        #Top pipe       
        self.pipeup_y = (self.pipedown_y - PIPE_SPACE) - PIPEDOWN.get_height() 
        self.pipeup_x = PIPES_START_POS
        self.pipeup_width = PIPEUP.get_width()
        self.pipeup_height = PIPEUP.get_height()

        self.pipeup_rect = pygame.Rect(self.pipeup_x, self.pipeup_y, self.pipeup_width, self.pipeup_height)
        self.pipedown_rect = pygame.Rect(self.pipedown_x, self.pipedown_y, self.pipedown_width, self.pipedown_height)


    def spawn(self):
        self.pipedown_rect.y  = random.randint(123, 514)
        self.pipeup_rect.y = (self.pipedown_rect.y - PIPE_SPACE) - PIPEDOWN.get_height()

    def movement(self, vel):
        for _ in range(self.obstacle_count):
            self.obstacle_list.append(self.pipedown_rect)

        for obstacle in self.obstacle_list:
            obstacle.x -= vel
            if obstacle.x < -70:
                self.obstacle_list.remove(obstacle)
        
        if len(self.obstacle_list) >= 3:
            self.obstacle_count = 3

        print(self.obstacle_list)
        print(len(self.obstacle_list))

    def draw(self, screen): #obstacle list has the rect of the image
        screen.blit(PIPEUP, (self.pipeup_rect.x , self.pipeup_rect.y ))
        obstacle_pos = 0
        obstacle_speed = 0.01
        obstacle_pos += obstacle_speed
        # screen.blit(PIPEDOWN, (self.obstacle_list[int(obstacle_pos)].x, self.obstacle_list[int(obstacle_pos)].y))

        if obstacle_pos > len(self.obstacle_list):
            obstacle_pos = 0

    def event_manager(self, event, vel, screen):
        if event.type == SPAWN_EVENT:
            pass

        
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
            self.bird_images.append(pygame.image.load(f"PYTHON/Learning/Games/flappy_folder/flappy/bird{x+1}.png").convert_alpha())

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

            # obstacle.event_manager(event, OBST_VEL, SCREEN)
        
        keys = pygame.key.get_pressed()

        draw_screen(SCREEN, blit_images)
        bird.draw(SCREEN)
        bird.move(keys)

        obstacle.movement(OBST_VEL)
        obstacle.draw(SCREEN)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
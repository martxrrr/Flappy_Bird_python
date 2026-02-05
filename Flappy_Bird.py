import pygame

WIDTH, HEIGHT = 900, 600
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LIST_LEN = 3
GROUND_BORDER = 115
BIRD = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bird1.png")
BIRD_WIDTH = BIRD.get_height()
BIRD_HEIGHT = BIRD.get_width()
BIRD_X, BIRD_Y = 100, 300

BG = pygame.transform.scale(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bg.png"), (WIDTH, HEIGHT))
GROUND = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/ground.png")
PIPEDOWN = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png")
PIPEUP = pygame.transform.rotate(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png"), 180)

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bird_list = []
        self.bird_count = 0
        self.animation_speed = 0.1
        self.jump_count = 9

    def draw_bird(self, screen):
        for x in range(LIST_LEN):
            self.bird_list.append(pygame.image.load(f"PYTHON/Learning/Games/flappy_folder/flappy/bird{x + 1}.png"))

        self.bird_count += self.animation_speed
        if self.bird_count > LIST_LEN: self.bird_count = 0
        screen.blit(self.bird_list[int(self.bird_count)], (self.x, self.y))

    def move(self):
        self.y += self.jump_count
        if self.y >= HEIGHT - GROUND_BORDER: self.y = HEIGHT - GROUND_BORDER
        if self.y < 0: self.y = 0

    def jump(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.jump_count
    
def main():

    def draw_window(screen):
        screen.blit(BG, (0,0))
        screen.blit(GROUND, (0, HEIGHT - (GROUND.get_height() / 2)))

    running = True
    clock = pygame.time.Clock()
    bird = Bird(BIRD_X, BIRD_Y)

    while running:
        clock.tick(FPS)
        up = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up = True
                if event.type == pygame.KEYUP:
                    up = False

        keys = pygame.key.get_pressed()
        if up == True:
            bird.jump(keys)
        if up == False:
            bird.move()

        draw_window(SCREEN)
        bird.draw_bird(SCREEN)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
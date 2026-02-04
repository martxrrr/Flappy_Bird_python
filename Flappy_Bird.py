import pygame

WIDTH, HEIGHT = 800, 400
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


BG = pygame.transform.scale(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/bg.png"), (WIDTH, HEIGHT))
GROUND = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/ground.png")
PIPEDOWN = pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png")
PIPEUP = pygame.transform.rotate(pygame.image.load("PYTHON/Learning/Games/flappy_folder/flappy/pipedown.png"), 180)


def draw_birds(screen):
    birds_list = [] 
    bird_count = 0
    animation_speed = 0.1
    for x in range(3):
        birds_list.append(pygame.image.load(f"PYTHON/Learning/Games/flappy_folder/flappy/bird{x + 1}.png"))

    bird_count += animation_speed
    # if bird_count > len(birds_list): bird_count = 0

    screen.blit(birds_list[int(bird_count)], (100, 100))
    print(bird_count)
    

def draw_window(screen):
    screen.blit(BG, (0,0))
    screen.blit(GROUND, (0, 350))

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window(SCREEN)
        draw_birds(SCREEN)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
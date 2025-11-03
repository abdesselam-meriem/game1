import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
        # Keep player inside left boundary
        if player.left < 0:
            player.left = 0
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
        # Keep player inside right boundary
        if player.right > SCREEN_WIDTH:
            player.right = SCREEN_WIDTH
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)
        # Keep player inside top boundary
        if player.top < 0:
            player.top = 0
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)
        # Keep player inside bottom boundary
        if player.bottom > SCREEN_HEIGHT:
            player.bottom = SCREEN_HEIGHT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
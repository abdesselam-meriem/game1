import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((50, 50, 50, 50))

#create walls (rectangles)
walls =  [
    pygame.Rect(0, 0, 1000, 20), #top horizontal wall
    pygame.Rect(0, 0, 20, 800), #left vertical wall
    pygame.Rect(980, 0, 20, 800), #middle horizontal wall
    pygame.Rect(0, 780, 1000, 20), #right vertical wall

    #inner maze walls
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 100, 20, 420), #column
    pygame.Rect(200, 480, 600, 20),
    pygame.Rect(580, 200, 20, 300), #column
    pygame.Rect(100, 650, 800, 20),
    pygame.Rect(900, 100, 20, 570), #column
    pygame.Rect(400, 300, 400, 20),
    pygame.Rect(200, 380, 200, 20),
    pygame.Rect(700, 380, 200, 20),

]

run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)

    for wall in walls:
        pygame.draw.rect(screen, (0, 255, 0), wall)


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

    for wall in walls:
        if player.colliderect (wall):
            if key[pygame.K_LEFT]:
                player.left = wall.right
            if key[pygame.K_RIGHT]:
                player.right = wall.left
            if key[pygame.K_UP]:
                player.top = wall.bottom
            if key[pygame.K_DOWN]:
                player.bottom = wall.top

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
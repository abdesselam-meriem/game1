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
    pygame.Rect(980, 0, 20, 800), #right vertical wall
    pygame.Rect(0, 780, 1000, 20), #bottom horizontal wall

    #inner maze walls
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 100, 20, 420),
    pygame.Rect(200, 480, 600, 20),
    pygame.Rect(580, 200, 20, 300),
    pygame.Rect(100, 650, 800, 20),
    pygame.Rect(900, 100, 20, 570),
    pygame.Rect(400, 300, 400, 20),
    pygame.Rect(200, 380, 200, 20),
    pygame.Rect(700, 380, 200, 20),
]

run = True
while run:
    screen.fill((0,0,0))
    
    # Draw walls first
    for wall in walls:
        pygame.draw.rect(screen, (0, 255, 0), wall)
    
    # Draw player on top
    pygame.draw.rect(screen, (255,0,0), player)

    # Store the player's position before moving
    old_x, old_y = player.x, player.y

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)
    elif key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)

    # Check for collisions after moving
    for wall in walls:
        if player.colliderect(wall):
            # If collision detected, revert to old position
            player.x, player.y = old_x, old_y
            break  # Stop checking other walls once we find a collision

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
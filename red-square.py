import pygame
import os

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Adventure")

# Load background images
def load_image(path, scale=True):
    try:
        image = pygame.image.load(path)
        if scale:
            image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        return image
    except:
        print(f"Error loading image: {path}")
        # Fallback: create a colored surface
        surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surf.fill((50, 50, 150))  # Dark blue fallback
        return surf

# Load your background images
welcome_bg = load_image("assets/cat.jpg")
level_select_bg = load_image("assets/sailormoon.jpg")
game_bg = load_image("assets/sakura.jpg")

# Game states
STATE_WELCOME = 0
STATE_LEVEL_SELECT = 1
STATE_PLAYING = 2
current_state = STATE_WELCOME

# Colors (adjust for better visibility on backgrounds)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 150, 255)
GOLD = (255, 215, 0)

# Fonts
title_font = pygame.font.SysFont('comicsansms', 72, bold=True)
button_font = pygame.font.SysFont('arial', 32)

# Enhanced Button class with better styling
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=WHITE, border_radius=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.is_hovered = False
        self.shadow_offset = 5
        
    def draw(self, surface):
        # Draw shadow
        shadow_rect = self.rect.move(self.shadow_offset, self.shadow_offset)
        pygame.draw.rect(surface, (30, 30, 30), shadow_rect, border_radius=self.border_radius)
        
        # Draw button
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=self.border_radius)
        
        # Draw text
        text_surf = button_font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        
    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click

# Create styled buttons
start_button = Button(400, 500, 200, 60, "Start Adventure", 
                     (0, 150, 0), (0, 255, 0), border_radius=15)

level1_button = Button(400, 350, 200, 60, "Level 1", 
                      (0, 0, 200), (0, 255, 255), border_radius=15) #JE DOIS CHANGER 

level2_button = Button(400, 450, 200, 60, "Level 2", 
                      (150, 0, 0), (255, 0, 0), border_radius=15)

back_button = Button(50, 700, 120, 50, "← Back", 
                    (128, 128, 128), (192, 192, 192), border_radius=10)

# Game elements
player = pygame.Rect(50, 50, 40, 40)

# Different mazes for levels
level1_walls = [
    pygame.Rect(0, 0, 1000, 20),
    pygame.Rect(0, 0, 20, 800),
    pygame.Rect(980, 0, 20, 800),
    pygame.Rect(0, 780, 1000, 20),


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

level2_walls = [
    pygame.Rect(0, 0, 1000, 20),
    pygame.Rect(0, 0, 20, 800),
    pygame.Rect(980, 0, 20, 800),
    pygame.Rect(0, 780, 1000, 20),


    pygame.Rect(100, 100, 20, 300),
    pygame.Rect(100, 100, 300, 20),
    pygame.Rect(380, 100, 300, 20),
    pygame.Rect(200, 200, 200, 20),
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(200, 380, 300, 20),
    pygame.Rect(480, 200, 20, 200),
    pygame.Rect(300, 300, 200, 20),

    pygame.Rect(600, 100, 20, 300),
    pygame.Rect(600, 100, 200, 20),
    pygame.Rect(780, 100, 20, 200),
    pygame.Rect(700, 100, 20, 200),
    pygame.Rect(700, 200, 100, 20),
    pygame.Rect(700, 380, 200, 20),
    pygame.Rect(880, 300, 20, 100),
    pygame.Rect(800, 300, 100, 20),
    
]

current_walls = level1_walls
current_level = 1

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_click = True
    
    # State management with backgrounds
    if current_state == STATE_WELCOME:
        # Draw welcome background
        screen.blit(welcome_bg, (0, 0))
        
        # Add semi-transparent overlay for better text visibility
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))  # Black with transparency
        screen.blit(overlay, (0, 0))
        
        # Draw title with shadow effect
        title_text = title_font.render("MAZE ADVENTURE", True, GOLD)
        title_shadow = title_font.render("MAZE ADVENTURE", True, (100, 80, 0))
        
        screen.blit(title_shadow, (SCREEN_WIDTH//2 - title_text.get_width()//2 + 3, 203))
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 200))
        
        # Draw subtitle
        subtitle_font = pygame.font.SysFont('arial', 24)
        subtitle = subtitle_font.render("Embark on an epic journey through mysterious mazes!", True, WHITE)
        screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, 300))
        
        # Update and draw button
        start_button.check_hover(mouse_pos)
        start_button.draw(screen)
        
        if start_button.is_clicked(mouse_pos, mouse_click):
            current_state = STATE_LEVEL_SELECT
            
    elif current_state == STATE_LEVEL_SELECT:
        # Draw level selection background
        screen.blit(level_select_bg, (0, 0))
        
        # Add overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        screen.blit(overlay, (0, 0))
        
        # Draw title
        title_text = title_font.render("Choose Your Level", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 150))
        
        # Update and draw buttons
        level1_button.check_hover(mouse_pos)
        level2_button.check_hover(mouse_pos)
        back_button.check_hover(mouse_pos)
        
        level1_button.draw(screen)
        level2_button.draw(screen)
        back_button.draw(screen)
        
        # Check button clicks
        if level1_button.is_clicked(mouse_pos, mouse_click):
            current_state = STATE_PLAYING
            current_level = 1
            current_walls = level1_walls
            player.x, player.y = 50, 50
        elif level2_button.is_clicked(mouse_pos, mouse_click):
            current_state = STATE_PLAYING
            current_level = 2
            current_walls = level2_walls
            player.x, player.y = 50, 50
        elif back_button.is_clicked(mouse_pos, mouse_click):
            current_state = STATE_WELCOME
            
    elif current_state == STATE_PLAYING:
        # Draw game background
        screen.blit(game_bg, (0, 0))
        
        # Draw walls with a style matching the theme
        for wall in current_walls:
            if current_level == 1:
                # Forest theme - green walls
                pygame.draw.rect(screen, (50, 120, 50), wall)
                # Add wall texture/outline
                pygame.draw.rect(screen, (30, 80, 30), wall, 3)
            else:
                # Castle theme - gray walls
                pygame.draw.rect(screen, (100, 100, 100), wall)
                pygame.draw.rect(screen, (70, 70, 70), wall, 3)
        
        # Draw player
        pygame.draw.rect(screen, RED, player)
        # Add player details
        pygame.draw.rect(screen, (200, 0, 0), player, 2)
        
        # Draw level info
        level_font = pygame.font.SysFont('arial', 24)
        level_text = level_font.render(f"Level {current_level}", True, WHITE)
        screen.blit(level_text, (20, 20))
        
        # Draw back button
        back_button.check_hover(mouse_pos)
        back_button.draw(screen)
        
        # Handle movement
        keys = pygame.key.get_pressed()
        old_x, old_y = player.x, player.y
        
        if keys[pygame.K_LEFT]:
            player.x -= 3
        if keys[pygame.K_RIGHT]:
            player.x += 3
        if keys[pygame.K_UP]:
            player.y -= 3
        if keys[pygame.K_DOWN]:
            player.y += 3
        
        # Check collisions
        for wall in current_walls:
            if player.colliderect(wall):
                player.x, player.y = old_x, old_y
                break
        
        # Check if back button is clicked
        if back_button.is_clicked(mouse_pos, mouse_click):
            current_state = STATE_LEVEL_SELECT
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
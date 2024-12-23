import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodger Game")

#이미지 불러오기
img_flight = pygame.image.load("flight.png")
img_flight = pygame.transform.scale(img_flight, (50, 50))

img_bullet = pygame.image.load("bullet.png")
img_bullet = pygame.transform.scale(img_bullet, (50, 50))




# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)



# Set up font
font = pygame.font.Font(None, 36)

# Function to draw the player
def draw_player(x, y):
    screen.blit(img_flight, (x, y))

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(img_bullet, obstacle)

# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Main game loop
clock = pygame.time.Clock()


def ingame():
    # Set up player
    player_size = 40
    player_x = width // 2 - player_size // 2
    player_y = height - player_size -10
    player_speed = 5

    # Set up obstacles
    obstacle_size = 50
    obstacle_speed = 5
    obstacle_frequency = 25
    obstacles = []

    timer = 0
    score = 0
    playing = True
    
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed
    
        # Spawn obstacles
        if random.randrange(obstacle_frequency) == 0:
            obstacle_x = random.randint(0, width - obstacle_size)
            obstacle_y = -obstacle_size-timer*0.2
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    
        # Move and remove obstacles
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > height:
                obstacles.remove(obstacle)
                score += 1
    
        # Check for collisions with obstacles
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                playing = False
        
    
        timer += 1
    
        # Clear the screen
        screen.fill(black)
    
        # Draw the player, obstacles, and score
        draw_player(player_x, player_y)
        draw_obstacles(obstacles)
        display_score(score)
    
        # Update the display
        pygame.display.flip()
    
        # Control the frame rate
        clock.tick(60)
        
    gameover(score)

def gameover(score):
    playing = True
    
    score_text = font.render("Score: " + str(score), True, white)
    restart_text = font.render("RESTART", True, black)
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 250):
                    playing = False
            
           
    

        screen.fill(black)
        
        screen.blit(score_text, (240, 150))
        pygame.draw.rect(screen, white, (200, 200, 200, 50))
        screen.blit(restart_text, (240, 210))
        pygame.display.flip()
        clock.tick(60)
        
    ingame()

    




ingame()
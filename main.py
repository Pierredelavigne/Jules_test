import pygame
import sys
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GREEN, WHITE, BROWN,
                    TABLE_MARGIN, TABLE_WIDTH, TABLE_HEIGHT, CUSHION_THICKNESS, POCKET_RADIUS, BALL_RADIUS)
from entities import Ball, Table

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu de Billard")

    clock = pygame.time.Clock()

    # Create the table
    game_table = Table(
        x=TABLE_MARGIN,
        y=TABLE_MARGIN,
        width=TABLE_WIDTH,
        height=TABLE_HEIGHT,
        cushion_thickness=CUSHION_THICKNESS,
        color=GREEN,
        cushion_color=BROWN,
        pocket_radius=POCKET_RADIUS
    )

    # Create a sample ball (cue ball)
    # Position it on the playing area of the table
    cue_ball_start_x = game_table.playing_area.left + game_table.playing_area.width / 4
    cue_ball_start_y = game_table.playing_area.centery
    cue_ball = Ball(cue_ball_start_x, cue_ball_start_y, WHITE, BALL_RADIUS)

    # Give it some initial speed for testing (will be removed later for player control)
    cue_ball.vx = 6
    cue_ball.vy = 2.5

    balls = [cue_ball]

    # Example of other balls (Red and Yellow for now)
    # These positions are approximate for initial setup
    balls.append(Ball(game_table.playing_area.centerx + 50, game_table.playing_area.centery - 20, (255,0,0), BALL_RADIUS))
    balls.append(Ball(game_table.playing_area.centerx + 80, game_table.playing_area.centery + 10, (255,255,0), BALL_RADIUS))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Add other event handling here (e.g., mouse clicks for shooting)

        # Game logic updates
        for ball in balls:
            ball.move()
            ball.check_cushion_collision(game_table.playing_area)
            # Pocketing logic will be added later
            # Ball-to-ball collision logic will be added later

        # Drawing code
        screen.fill(BLACK)  # Background color for areas outside the table

        game_table.draw(screen) # Draw the table first

        # Draw balls
        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

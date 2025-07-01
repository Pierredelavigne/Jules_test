import pygame
from config import BALL_RADIUS, WHITE, FRICTION

class Ball:
    def __init__(self, x, y, color=WHITE, radius=BALL_RADIUS):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vx = 0  # Velocity in x direction
        self.vy = 0  # Velocity in y direction
        self.is_active = True # To check if the ball is on table or pocketed

    def draw(self, screen):
        """Draws the ball on the screen."""
        if self.is_active:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        """Updates the ball's position based on its velocity and applies friction."""
        if self.is_active:
            self.x += self.vx
            self.y += self.vy

            # Apply friction
            self.vx *= FRICTION
            self.vy *= FRICTION

            # Stop the ball if velocity is very low to prevent endless rolling
            if abs(self.vx) < 0.05 and abs(self.vy) < 0.05:
                self.vx = 0
                self.vy = 0

    def check_cushion_collision(self, table_playing_area):
        """Checks and handles collision with table cushions."""
        if not self.is_active:
            return

        # Left cushion
        if self.x - self.radius <= table_playing_area.left:
            self.x = table_playing_area.left + self.radius
            self.vx *= -1
        # Right cushion
        elif self.x + self.radius >= table_playing_area.right:
            self.x = table_playing_area.right - self.radius
            self.vx *= -1
        # Top cushion
        if self.y - self.radius <= table_playing_area.top:
            self.y = table_playing_area.top + self.radius
            self.vy *= -1
        # Bottom cushion
        elif self.y + self.radius >= table_playing_area.bottom:
            self.y = table_playing_area.bottom - self.radius
            self.vy *= -1

    def __repr__(self):
        return f"Ball(x={self.x}, y={self.y}, vx={self.vx}, vy={self.vy}, color={self.color})"


class Table:
    def __init__(self, x, y, width, height, cushion_thickness, color, cushion_color, pocket_radius):
        self.rect = pygame.Rect(x, y, width, height)
        self.cushion_thickness = cushion_thickness
        self.color = color
        self.cushion_color = cushion_color
        self.pocket_radius = pocket_radius

        # Define playing area (inside cushions)
        self.playing_area = pygame.Rect(
            x + cushion_thickness,
            y + cushion_thickness,
            width - 2 * cushion_thickness,
            height - 2 * cushion_thickness
        )

        # Define pockets (corners and middle for a standard table)
        # Coordinates are relative to the screen, not the table rect itself for easier drawing
        self.pockets = [
            (x + pocket_radius, y + pocket_radius),  # Top-left
            (x + width / 2, y + pocket_radius / 2), # Top-middle (approximation for drawing)
            (x + width - pocket_radius, y + pocket_radius),  # Top-right
            (x + pocket_radius, y + height - pocket_radius),  # Bottom-left
            (x + width / 2, y + height - pocket_radius / 2), # Bottom-middle (approximation)
            (x + width - pocket_radius, y + height - pocket_radius)   # Bottom-right
        ]
        # For simplicity, middle pockets are drawn slightly into the cushion area
        # A more precise model would have cutouts in the cushions

    def draw(self, screen):
        # Draw table bed
        pygame.draw.rect(screen, self.color, self.rect)

        # Draw cushions (as 4 rectangles inside the main table rect)
        # Top cushion
        pygame.draw.rect(screen, self.cushion_color, (self.rect.left, self.rect.top, self.rect.width, self.cushion_thickness))
        # Bottom cushion
        pygame.draw.rect(screen, self.cushion_color, (self.rect.left, self.rect.bottom - self.cushion_thickness, self.rect.width, self.cushion_thickness))
        # Left cushion
        pygame.draw.rect(screen, self.cushion_color, (self.rect.left, self.rect.top, self.cushion_thickness, self.rect.height))
        # Right cushion
        pygame.draw.rect(screen, self.cushion_color, (self.rect.right - self.cushion_thickness, self.rect.top, self.cushion_thickness, self.rect.height))

        # Draw playing surface over cushions to get sharp inner edges
        pygame.draw.rect(screen, self.color, self.playing_area)

        # Draw pockets
        for pocket_pos in self.pockets:
            pygame.draw.circle(screen, BLACK, (int(pocket_pos[0]), int(pocket_pos[1])), self.pocket_radius)

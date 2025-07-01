# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)  # Table color
BROWN = (139, 69, 19) # Cushion color

# Ball properties
BALL_RADIUS = 10 # Reduced for better visual fit with pockets

# Table properties
TABLE_MARGIN = 50 # Margin from screen edge to table
TABLE_WIDTH = SCREEN_WIDTH - 2 * TABLE_MARGIN
TABLE_HEIGHT = SCREEN_HEIGHT - 2 * TABLE_MARGIN
CUSHION_THICKNESS = 20
POCKET_RADIUS = 22 # Slightly larger than ball radius

# Physics
FRICTION = 0.99 # factor to reduce speed each frame, increased friction slightly

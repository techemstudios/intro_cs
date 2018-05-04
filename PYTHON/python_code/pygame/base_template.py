"""
Simple template to open a pygame window
orginal from programarcadegames.com
"""

import pygame

# Define colors
# Color   R    G    B
WHITE = (255, 255, 255)

pygame.init()

# Set window height and width
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set caption that appears at top of window
pygame.display.set_caption("This is my game!")

# Set up a "flag", loop until the user closes the window
done = False

# manage how fast the screen updates
clock = pygame.time.Clock()

# The MAIN program loop
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Make the background a certain color
    screen.fill(WHITE)

    # Update the screen with what has been drawn so far
    pygame.display.update()

    # 60 frames per second limit
    clock.tick(60)

# Close the window to quit
pygame.quit()


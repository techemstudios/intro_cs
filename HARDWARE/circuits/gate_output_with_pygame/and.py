"""
Python representation of a simple AND gate.

Uses pygame to display a lightbulb image that represents the output value 
of an AND gate.  
"""

import sys, pygame
from pygame.locals import *
pygame.init()

def AND():
        # input one
    a = int(raw_input("INPUT A = ENTER <0> or <1>: "))
        # input two
    b = int(raw_input("INPUT B = ENTER <0> or <1>: "))

    if a and b > 0:
        print("\tSince A AND B are both True...")
        print("\tOUTPUT = TRUE")

            # window size
        size = width, height = 600, 600
            # set speed
        speed = [1, 1]
            # create a variable color
        color = (0, 0, 0)
            # tell Python the type of screen
        screen = pygame.display.set_mode(size)
            # set variable for image
            # and tell Python the file name to get
        light = pygame.image.load("light_on.jpg")
            # set variable 
        lightrect = light.get_rect()
        lightrect.centerx = 300
        lightrect.centery = 325
        lightrect.center

            # setup the loop
        while 1:
                # fill the background with the color specified earlier
            screen.fill(color)
            sys_font = pygame.font.SysFont("source code", 32)
            rendered = sys_font.render('OUTPUT = TRUE!', 0, (255, 100, 100))
            screen.blit(rendered, (205, 25))
                # draw image file to screen
            screen.blit(light, lightrect)
            pygame.display.flip()
        
    else:
        print("\tSince A AND B are both not True...")
        print("\tOUTPUT = FALSE")
        size = width, height = 600, 600
        speed = [1, 1]
        color = (0, 0, 0)
        screen = pygame.display.set_mode(size)
        light = pygame.image.load("light_off.jpg")
        lightrect = light.get_rect()
        lightrect.centerx = 300
        lightrect.centery = 325
        lightrect.center
        while 1:
            screen.fill(color)
            sys_font = pygame.font.SysFont("None", 32)
            rendered = sys_font.render('OUTPUT = FALSE!', 0, (255, 100, 100))
            screen.blit(rendered, (205, 25))
            screen.blit(light, lightrect)
            pygame.display.flip()

AND()



## Use this to animate the image (bounces)
##while 1:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT: sys.exit()
##
##    ballrect = ballrect.move(speed)
##    if ballrect.left < 0 or ballrect.right > width:
##        speed[0] = -speed[0]
##    if ballrect.top < 0 or ballrect.bottom > height:
##        speed[1] = -speed[1]



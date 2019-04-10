#! /usr/bin env python3
# coding: utf-8


"""
Mac Giver game :
Game where the player has to move Mac Giver through a maze with the cursor keys.
Before trying to escape, he has to collect 3 objects on his way.

Python script.
files : MacGyver.py, classes.py, cons.py, maze.txt, images
"""


# Modules importation

import pygame
from pygame.locals import *
from classes import *
from cons import *

def main():
    # Library initialization
    pygame.init()

    # Window creation
    window = pygame.display.set_mode((window_size, window_size))

    # Background filling
    bckg = pygame.image.load(image_background).convert()
    window.blit(bckg, (0, 0))

    # Maze setting
    maze = Maze("maze")
    window.blit(maze)

    # Mac Giver setting
    mc_giver = Player(image_mg)
    mg_position = mc_giver.position
    window.blit(mc_giver, mg_position)

    # Screen refresh
    pygame.display.flip()

    # Cont setting true (to continue)
    cont = 1

    # Keeping the window opened until event QUIT happens (Alt + F4 or close cross)
    while cont:

        for event in pygame.event.get():

            if event.type == QUIT:
                cont = 0
            elif event.type == KEYDOWN:  # What happens if user press a key down
                if event.key == K_DOWN:  # If down cursor key
                    mg_position = mg_position.move('down')  # Mg goes down for 1 sprite
                elif event.key == K_UP:  # If up cursor key
                    mg_position = mg_position.move('up')  # Mg goes up for 1 sprite
                elif event.key == K_RIGHT:  # If right cursor key
                    mg_position = mg_position.move('right')  # Mg goes right for 1 sprite
                elif event.key == K_LEFT:  # If left cursor key
                    mg_position = mg_position.move('left')  # Mg goes left for 1 sprite


if __name__ == __main__:
    main()

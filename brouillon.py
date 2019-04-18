#! /usr/bin env python3
# coding: utf-8


"""
Mac Giver game :
Game where the player has to move Mac Giver through a maze with the cursor keys.
Before trying to escape, he has to collect 3 objects on his way.

Python script.
files : MacGyver.py, classes.py, cons.py, maze.txt, images
"""


# Modules importation.

import pygame
from pygame.locals import *
from cons import *
from maze import Maze
from items import Player
from items import Collected


# Library initialization.
pygame.init()

# Window creation.
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Mac Gyver")


# Maze setting.
maze = Maze("maze.txt")
maze.initialize_maze()
maze.display(window)

# Mac Giver setting.
mc_giver = Player(image_mg)
mg_position = mc_giver.position
mc_giver.show(window)

# objects setting.
ether = Collected(image_ether)
ether.position = ether.init_position(maze)
ether.show(window)
needle = Collected(image_needle)
needle.position = needle.init_position(maze)
needle.show(window)
plastic_pipe = Collected(image_plastic_pipe)
plastic_pipe.position = plastic_pipe.init_position(maze)
plastic_pipe.show(window)

# Screen refresh.
pygame.display.flip()

# Cont setting true (to continue).
cont = 1


# display of the end of the game
def text_display(text):
    """method to display text in the window
    :param : text : text to display"""
    font = pygame.font.Font(None, 32)
    i = 0
    for line in text.splitlines():
        i += sprite_size
        text = font.render(line, 1, (0, 0, 0))
        text_rect = text.get_rect(center=(window_size / 2, (window_size / 4) + i))
        window.blit(text, text_rect)
        pygame.display.flip()
    pygame.time.wait(3000)


# Keeping the window opened until event QUIT happens (Alt + F4 or close cross), or until the maze is finished.
while cont:
    pygame.time.Clock().tick(30)  # Saving processor resources.
    for event in pygame.event.get():
        if event.type == QUIT:  # If event QUIT, we go out of the while loop.
            cont = 0
        elif event.type == KEYDOWN:  # What happens if user press a key down.
            if event.key == K_DOWN:  # If down cursor key.
                mg_position = mc_giver.move('down', maze)  # Mg goes down for 1 sprite.
            elif event.key == K_UP:  # If up cursor key.
                mg_position = mc_giver.move('up', maze)  # Mg goes up for 1 sprite.
            elif event.key == K_RIGHT:  # If right cursor key.
                mg_position = mc_giver.move('right', maze)  # Mg goes right for 1 sprite.
            elif event.key == K_LEFT:  # If left cursor key.
                mg_position = mc_giver.move('left', maze)  # Mg goes left for 1 sprite.

        if mg_position == ether.position:  # Mac Gyver picked the ether.
            ether.exists = 0
        elif mg_position == needle.position:  # Mac Gyver picked the needle.
            needle.exists = 0
        elif mg_position == plastic_pipe.position:  # Mac Gyver picked the plastic pipe.
            plastic_pipe.exists = 0

        # Re-pasting after the event loop.
        maze.display(window)
        mc_giver.show(window)
        if ether.exists != 0:  # Not picked by Mac Gyver.
            ether.show(window)
        if needle.exists != 0:  # Not picked by Mac Gyver.
            needle.show(window)
        if plastic_pipe.exists != 0:  # Not picked by Mac Gyver.
            plastic_pipe.show(window)

        # Screen refresh.
        pygame.display.flip()

        # When Mac Gyver arrives to the guard position (sprite "a").
        if maze.structure[mc_giver.sprite_y][mc_giver.sprite_x] == "a":
            # We check if there are still objects to pick in the maze
            if ether.exists or needle.exists or plastic_pipe.exists:
                text_display("Vous vous êtes présenté devant le garde \n"
                             "sans les armes nécessaires, \n"
                             "vous avez perdu !")
            # If not, the player has won.
            else:
                text_display("Bravo ! \n"
                             "À l'aide de la seringue que vous avez fabriquée, \n"
                             "vous avez vaincu le garde et vous vous échapez !")

            # We go out of the While loop
            cont = 0


# Closes the window.
pygame.quit()

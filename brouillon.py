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


# Library initialization
pygame.init()

# Window creation
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Mac Gyver")


# Maze setting
maze = Maze("maze.txt")
maze.initialize_maze()
maze.display(window)

# Mac Giver setting
mc_giver = Player(image_mg)
mg_position = mc_giver.position
mc_giver.show(window)

# objects setting
ether = Collected(image_ether)
ether.position = ether.init_position(maze)
ether.show(window)
needle = Collected(image_needle)
needle.position = needle.init_position(maze)
needle.show(window)
plastic_pipe = Collected(image_plastic_pipe)
plastic_pipe.position = plastic_pipe.init_position(maze)
plastic_pipe.show(window)

# Screen refresh
pygame.display.flip()

# Cont setting true (to continue)
cont = 1

# Keeping the window opened until event QUIT happens (Alt + F4 or close cross)
while cont:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():

        if event.type == QUIT:
            cont = 0
        elif event.type == KEYDOWN:  # What happens if user press a key down
            if event.key == K_DOWN:  # If down cursor key
                mg_position = mc_giver.move('down', maze)  # Mg goes down for 1 sprite
            elif event.key == K_UP:  # If up cursor key
                mg_position = mc_giver.move('up', maze)  # Mg goes up for 1 sprite
            elif event.key == K_RIGHT:  # If right cursor key
                mg_position = mc_giver.move('right', maze)  # Mg goes right for 1 sprite
            elif event.key == K_LEFT:  # If left cursor key
                mg_position = mc_giver.move('left', maze)  # Mg goes left for 1 sprite

        if mg_position == ether.position:
            ether.exists = 0
        elif mg_position == needle.position:
            needle.exists = 0
        elif mg_position == plastic_pipe.position:
            plastic_pipe.exists = 0

        maze.display(window)
        mc_giver.show(window)
        if ether.exists != 0:
            ether.show(window)
        if needle.exists != 0:
            needle.show(window)
        if plastic_pipe.exists != 0:
            plastic_pipe.show(window)
        pygame.display.flip()

        if maze.structure[mc_giver.sprite_y][mc_giver.sprite_x] == "a":
            if ether.exists or needle.exists or plastic_pipe.exists:
                print("vous avez affronté le garde sans les armes nécessaires, vous êtes mort !!!")
            else:
                print("bravo !!!")




#! /usr/bin env python3
# coding: utf-8

"""File containing the class Maze, used to create the maze."""

import pygame
from cons import *


class Maze(object):
    """Class used to create the maze.
    :param : file : file where is written the structure of the maze"""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def initialize_maze(self):
        """Method used to generate the maze from the txt file:
        A list is created, containing one list by line contained in the file."""
        # We open the file and create the list of lines.
        with open(self.file, "r") as file:
            lines_n = []
            # We browse the lines of the file and create one list by line.
            for line in file:
                line_n = []
                # We browse the sprites (symbolized by letters) in the file.
                for sprite in line.strip():
                    # We add the sprite to the list.
                    line_n.append(sprite)
                # We add the list of the line to the lines list.
                lines_n.append(line_n)
            # We save the structure of the maze.
            self.structure = lines_n

    def display(self, window):
        """Method used to display  the maze from the list we generated with the method initialize_maze.
        :param : window : window where the maze is displayed"""
        # images (image of the arrival is the image of the guard standing on the arrival sprite).
        wall = pygame.image.load(IMAGE_WALL).convert()
        wall = pygame.transform.scale(wall, (SPRITE_SIZE, SPRITE_SIZE))
        arrival = pygame.image.load(IMAGE_GUARD).convert()
        arrival = pygame.transform.scale(arrival, (SPRITE_SIZE, SPRITE_SIZE))
        background = pygame.image.load(IMAGE_BACKGROUND).convert()
        background = pygame.transform.scale(background, (SPRITE_SIZE, SPRITE_SIZE))

        # We browse the list we created with initialize_maze.
        line_num = 0
        for line in self.structure:
            # We browse the list of sprites
            sprite_num = 0
            for sprite in line:
                # We calculate the real position (in pixels).
                x = sprite_num * SPRITE_SIZE
                y = line_num * SPRITE_SIZE
                if sprite == 'w':  # w = wall
                    window.blit(wall, (x, y))
                elif sprite == 'a':  # a = arrival
                    window.blit(arrival, (x, y))
                elif (sprite == '0') or (sprite == 'd'):  # 0 = path
                    window.blit(background, (x, y))
                sprite_num += 1
            line_num += 1

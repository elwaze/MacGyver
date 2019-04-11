#! /usr/bin env python3
# coding: utf-8


"""
File containing classes used in MacGyver.py.
"""


import pygame
from pygame.locals import *
from cons import *
from random import randint


class Maze:
    """Class used to create the maze."""

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
                for sprite in line:
                    # We ignore the line breaks.
                    if sprite != '\n':
                        # We add the sprite to the list.
                        line_n.append(sprite)
                # We add the list of the line to the lines list.
                lines_n.append(line_n)
            # We save the structure of the maze.
            self.structure = lines_n

    def display(self, window):
        """Method used to display  the maze from the list we generated with the method initialize_maze."""
        # images (image of the arrival is the image of the guard standing on the arrival sprite).
        wall = pygame.image.load(image_wall).convert()
        wall = pygame.transform.scale(wall, (sprite_size, sprite_size))
        arrival = pygame.image.load(image_guard).convert()
        arrival = pygame.transform.scale(arrival, (sprite_size, sprite_size))
        background = pygame.image.load(image_background).convert()
        background = pygame.transform.scale(background, (sprite_size, sprite_size))

        # We browse the list we created with initialize_maze.
        line_num = 0
        for line in self.structure:
            # We browse the list of sprites
            sprite_num = 0
            for sprite in line:
                # We calculate the real position (in pixels).
                x = sprite_num * sprite_size
                y = line_num * sprite_size
                if sprite == 'w':  # w = wall
                    window.blit(wall, (x, y))
                elif sprite == 'a':  # a = arrival
                    window.blit(arrival, (x, y))
                elif (sprite == '0') or (sprite == 'd'):  # 0 = couloir
                    window.blit(background, (x, y))
                sprite_num += 1
            line_num += 1


class Player:
    """Class used to create Mac Gyver."""

    def __init__(self, portrait):
        # Player's image.
        self.portrait = pygame.image.load(portrait).convert()
        self.portrait = pygame.transform.scale(self.portrait, (sprite_size, sprite_size))

        # Player's position (in sprites and in pixels).
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_y * sprite_size
        self.position = self.x, self.y
        # number of objects collected (counter).
        self.obj = 0

    def show(self, window):
        """Method used to display the player."""
        window.blit(self.portrait, self.position)

    def move(self, direction, model):
        """Method used to move the player."""

        # Moving to the right.
        if direction == 'right':
            # Staying in the window.
            if self.sprite_x < (size_in_sprites - 1):
                # Not going into a wall
                if model.structure[self.sprite_y][self.sprite_x + 1] != 'w':
                    # Moving one sprite right
                    self.sprite_x += 1

        # Moving to the left
        if direction == 'left':
            if self.sprite_x > 0:
                if model.structure[self.sprite_y][self.sprite_x - 1] != 'w':
                    self.sprite_x -= 1

        # Moving up
        if direction == 'up':
            if self.sprite_y > 0:
                if model.structure[self.sprite_y - 1][self.sprite_x] != 'w':
                    self.sprite_y -= 1

        # Moving down
        if direction == 'down':
            if self.sprite_y < (size_in_sprites - 1):
                if model.structure[self.sprite_y + 1][self.sprite_x] != 'w':
                    self.sprite_y += 1

        # New position.
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_y * sprite_size
        self.position = self.x, self.y

        return self.position


class Collected:
    """Class used to generate the objects that Mac Gyver has to collect."""

    def __init__(self, img):
        # Object image
        self.img = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(self.img, (sprite_size, sprite_size))

        # Object position initialization.
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_x * sprite_size
        self.position = self.x, self.y

        # Object position defined ?.
        self.exists = 0

    def init_position(self, model):
        """Random initialization of the position of the objects."""
        while self.exists == 0:          # While no valid position has been defined.
            self.sprite_x = randint(0, size_in_sprites - 1)          # x = random integer in the length of the window
            self.sprite_y = randint(0, size_in_sprites - 1)          # y = random integer in the height of the window
            if model.structure[self.sprite_y][self.sprite_x] == '0':    # In a couloir.
                self.exists = 1     # We have defined a valid position for this object
                self.x = self.sprite_x * sprite_size
                self.y = self.sprite_y * sprite_size
                self.position = self.x, self.y

        return self.position

    def show(self, window):
        """Method used to display the objects."""
        window.blit(self.img, self.position)

#! /usr/bin env python3
# coding: utf-8


"""
File containing classes used in MacGyver.py.
"""


import pygame
from pygame.locals import *
from cons import *
from random import randint





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
            if model.structure[self.sprite_y][self.sprite_x] == '0':    # In a passage.
                self.exists = 1     # We have defined a valid position for this object
                self.x = self.sprite_x * sprite_size
                self.y = self.sprite_y * sprite_size
                self.position = self.x, self.y

        return self.position

    def show(self, window):
        """Method used to display the objects."""
        window.blit(self.img, self.position)

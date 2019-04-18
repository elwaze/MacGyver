#! /usr/bin env python3
# coding: utf-8

"""File containing the superclass Items, and its subclasses Player and Collected.
Player is used to create MacGyver.
Collected is used to generate the items MacGyver has to collect. """

import pygame
from cons import *
from random import randint


class Item(object):
    """Superclass defining the display and the position of the items appearing in the game.
    Subclasses = Player and Collected. """

    def __init__(self, portrait):
        # Item's image.
        self.image = pygame.image.load(portrait).convert()
        self.image = pygame.transform.scale(self.image, (sprite_size, sprite_size))
        # Item's position.
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_y * sprite_size
        self.position = self.x, self.y

    def show(self, window):
        """Method used to display the item
        :param : window : window where the game is displayed. """
        window.blit(self.image, self.position)


class Player(Item):
    """Class used to create Mac Gyver. """

    def __init__(self, image):
        super().__init__(image)

    def move(self, direction, maze):
        """Method used to move the player.
        :param : direction : direction defined by the key pressed.
        :param : maze : model of the maze. """

        # Moving to the right.
        if direction == 'right':
            # Staying in the window.
            if self.sprite_x < (size_in_sprites - 1):
                # Not going into a wall
                if maze.structure[self.sprite_y][self.sprite_x + 1] != 'w':
                    # Moving one sprite right
                    self.sprite_x += 1

        # Moving to the left
        if direction == 'left':
            if self.sprite_x > 0:
                if maze.structure[self.sprite_y][self.sprite_x - 1] != 'w':
                    self.sprite_x -= 1

        # Moving up
        if direction == 'up':
            if self.sprite_y > 0:
                if maze.structure[self.sprite_y - 1][self.sprite_x] != 'w':
                    self.sprite_y -= 1

        # Moving down
        if direction == 'down':
            if self.sprite_y < (size_in_sprites - 1):
                if maze.structure[self.sprite_y + 1][self.sprite_x] != 'w':
                    self.sprite_y += 1

        # New position.
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_y * sprite_size
        self.position = self.x, self.y

        return self.position


class Collected(Item):
    """Class used to generate the objects that Mac Gyver has to collect."""

    def __init__(self, image):
        super().__init__(image)
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

#! /usr/bin env python3
# coding: utf-8

"""File containing the superclass ItemBase,
and its subclasses Player and Item.
Player is used to create MacGyver.
Item is used to generate
the items MacGyver has to collect.

"""

import pygame
import cons

from random import randint


class ItemBase(object):
    """Superclass defining the display and the
    position of the items appearing in the game.
    Subclasses = Player and Item.

    """

    def __init__(self, portrait):
        """Constructor.

        :param portrait: file containing the image of the item.

        """

        # Item's image.
        self.image = pygame.image.load(portrait).convert()
        self.image = pygame.transform.scale(
            self.image, (cons.SPRITE_SIZE, cons.SPRITE_SIZE))
        # Item's position.
        self.sprite_x = 0
        self.sprite_y = 0
        self.s_p = self.sprite_x, self.sprite_y
        self.x = self.sprite_x * cons.SPRITE_SIZE
        self.y = self.sprite_y * cons.SPRITE_SIZE
        self.position = self.x, self.y

    def show(self, window):
        """Method used to display the item

        :param window: window on which the game is displayed.

        """

        window.blit(self.image, self.position)


class Player(ItemBase):
    """Class used to create Mac Gyver.
    It's an ItemBase's child.

    """

    def __init__(self, image):
        """Constructor.
        :param image: file containing the image of the player.

        """

        super().__init__(image)

    def move(self, direction, maze):
        """Method used to move the player.

        :param direction: direction defined by the key pressed.
        :param maze: model of the maze.

        """

        # Moving to the right.
        if direction == 'right':
            # Staying in the window.
            if self.sprite_x < (cons.SIZE_IN_SPRITES - 1):
                # Not going into a wall
                if maze.structure[self.sprite_y][self.sprite_x + 1] != 'w':
                    # Moving one sprite right
                    self.sprite_x += 1

        # Moving to the left.
        if direction == 'left':
            if self.sprite_x > 0:
                if maze.structure[self.sprite_y][self.sprite_x - 1] != 'w':
                    self.sprite_x -= 1

        # Moving up.
        if direction == 'up':
            if self.sprite_y > 0:
                if maze.structure[self.sprite_y - 1][self.sprite_x] != 'w':
                    self.sprite_y -= 1

        # Moving down.
        if direction == 'down':
            if self.sprite_y < (cons.SIZE_IN_SPRITES - 1):
                if maze.structure[self.sprite_y + 1][self.sprite_x] != 'w':
                    self.sprite_y += 1

        # New position.
        self.x = self.sprite_x * cons.SPRITE_SIZE
        self.y = self.sprite_y * cons.SPRITE_SIZE
        self.position = self.x, self.y

        return self.position


class Item(ItemBase):
    """Class used to generate the objects that Mac Gyver has to collect.
    It's an ItemBase's child.

    """

    def __init__(self, image):
        """Constructor.

        :param image: file containing the image of the item.

        """

        super().__init__(image)
        # Object position not yet defined.
        self.exists = 0

    def init_position(self, model):
        """Random initialization of the position of the objects.

        :param model: model of the maze.

        """

        # While no valid position has been defined.
        while self.exists == 0:
            # x = random integer in the length of the window.
            self.sprite_x = randint(0, cons.SIZE_IN_SPRITES - 1)
            # y = random integer in the height of the window.
            self.sprite_y = randint(0, cons.SIZE_IN_SPRITES - 1)
            # In a passage, no other object on this sprite.
            if model.structure[self.sprite_y][self.sprite_x] == '0':
                # Mark the sprite to forbid it for other objects.
                model.structure[self.sprite_y][self.sprite_x] = 'x'
                # We have defined a valid position for this object.
                self.exists = 1
                self.x = self.sprite_x * cons.SPRITE_SIZE
                self.y = self.sprite_y * cons.SPRITE_SIZE
                self.position = self.x, self.y

        return self.position

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
        self.structure = 0

    @classmethod
    def initialize_maze(cls):
        """Method used to generate the maze from the txt file:
        A list is created, containing one list by line contained in the file."""
        # We open the file and create the list of lines.
        with open(cls.file, "r") as file:
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
            cls.structure = lines_n

    @classmethod
    def display(cls, window):
        """Method used to display  the maze from the list we generated with the method initialize_maze."""
        # images (image of the arrival ist the image of the guard standing on the arrival sprite).
        wall = pygame.image.load(image_wall).convert()
        arrival = pygame.image.load(image_guard).convert_alpha()

        # We browse the list we created with initialize_maze.
        line_num = 0
        for line in cls.structure:
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
                sprite_num += 1
            line_num += 1


class Player:
    """Class used to create Mac Gyver"""

    def __init__(self, portrait):
        # image du personnage
        self.portrait = pygame.image.load(portrait).convert_alpha()
        # Position du personnage en cases et en pixels
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = 0
        self.y = 0
        # number of objects collected
        self.obj = 0

    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""

        # Déplacement vers la droite
        if direction == 'right':
            # Pour ne pas dépasser l'écran
            if self.sprite_x < (size_in_sprites - 1):
                # On vérifie que la case de destination n'est pas un mur
                if maze.structure[self.sprite_y][self.sprite_x + 1] != 'w':
                    # Déplacement d'une case
                    self.sprite_x += 1
                    # Calcul de la position "réelle" en pixel
                    self.x = self.sprite_x * sprite_size

        # Déplacement vers la gauche
        if direction == 'left':
            if self.sprite_x > 0:
                if maze.structure[self.sprite_y][self.sprite_x - 1] != 'w':
                    self.sprite_x -= 1
                    self.x = self.sprite_x * sprite_size

        # Déplacement vers le haut
        if direction == 'up':
            if self.sprite_y > 0:
                if maze.structure[self.sprite_y - 1][self.sprite_x] != 'w':
                    self.sprite_y -= 1
                    self.y = self.sprite_y * sprite_size

        # Déplacement vers le bas
        if direction == 'down':
            if self.sprite_y < (size_in_sprites - 1):
                if maze.structure[self.sprite_y + 1][self.sprite_x] != 'w':
                    self.sprite_y += 1
                    self.y = self.sprite_y * sprite_size


class Collected:
    """Class used to generate the objects that Mac Gyver has to collect"""

    def __init__(self, img):
        # object image
        self.img = pygame.image.load(img).convert_alpha()
        # Position du personnage en cases et en pixels
        self.position = 0

    def init_position(self):
        # Position de l'obj en cases et en pixels
        while position == 0:          # tant que l'obj n'a pas de position
            self.sprite_x = randint(0, size_in_sprites - 1)          # x = entier au hasard ds la lgr
            self.sprite_y = randint(0, size_in_sprites - 1)          # y = entier au hazard ds la htr
            if maze.structure[self.sprite_y][self.sprite_x] != 'w':
                if maze.structure[self.sprite_y][self.sprite_x] != 'a':
                    position = 1
        self.x = self.sprite_x * sprite_size
        self.y = self.sprite_x * sprite_size

    def picked(self):
        # suppr un obj qd mg passe dessus



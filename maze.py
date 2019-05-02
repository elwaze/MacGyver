#! /usr/bin env python3
# coding: utf-8

"""File containing the class Maze, used to create the maze."""

import pygame
import cons


class Maze(object):
    """Class used to create the maze.
    :param : file : file where is written the structure of the maze"""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def initialize_maze(self):
        """Method used to generate the maze from the txt file:
        A list is created,
        containing one list by line contained in the file."""
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
        """Method used to display  the maze
        from the list we generated with the method initialize_maze.
        :param : window : window where the maze is displayed"""
        # Images:
        # image of the arrival is image of the guard
        # standing on the arrival sprite.
        wall = pygame.image.load(cons.IMAGE_WALL).convert()
        wall = pygame.transform.scale(
            wall, (cons.SPRITE_SIZE, cons.SPRITE_SIZE))
        arrival = pygame.image.load(
            cons.IMAGE_GUARD).convert()
        arrival = pygame.transform.scale(
            arrival, (cons.SPRITE_SIZE, cons.SPRITE_SIZE))
        background = pygame.image.load(
            cons.IMAGE_BACKGROUND).convert()
        background = pygame.transform.scale(
            background, (cons.SPRITE_SIZE, cons.SPRITE_SIZE))

        # We browse the list we created with initialize_maze.
        line_num = 0
        for line in self.structure:
            # We browse the list of sprites.
            sprite_num = 0
            for sprite in line:
                # We calculate the real position (in pixels).
                x = sprite_num * cons.SPRITE_SIZE
                y = line_num * cons.SPRITE_SIZE
                # w = wall.
                if sprite == 'w':
                    window.blit(wall, (x, y))
                # a = arrival.
                elif sprite == 'a':
                    window.blit(arrival, (x, y))
                # 0 = path
                elif (sprite == '0') or (sprite == 'd') or (sprite == "x"):
                    window.blit(background, (x, y))
                sprite_num += 1
            line_num += 1

    # display of the end of the game
    def text_display(self, window, text):
        """method to display text in the window
        :param: text: text to display"""

        # Replacing the maze by a simple background.
        background = pygame.Surface((cons.WINDOW_SIZE, cons.WINDOW_SIZE))
        background.fill((255, 100, 0))
        window.blit(background, (0, 0))

        # Displaying the text depending on the outcome of the game.
        font = pygame.font.Font(cons.FONT, 36)
        i = 0
        for line in text.splitlines():
            i += cons.SPRITE_SIZE
            text = font.render(line, 1, (0, 0, 0))
            text_rect = text.get_rect(center=(cons.WINDOW_SIZE / 2, (cons.WINDOW_SIZE / 4) + i))
            window.blit(text, text_rect)
            pygame.display.flip()
        pygame.time.wait(4000)

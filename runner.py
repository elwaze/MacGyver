#! /usr/bin env python3
# coding: utf-8

"""
File containing the class Runner.
Used to initialise the elements of the maze and
run the loop playing the game.

"""

import cons
import pygame.locals

from maze import Maze
from items import Player
from items import Item


class Runner(object):
    """Class used to initialize the elements of the maze and
    run the loop playing the game.

    """

    def __init__(self):

        # Library initialization.
        pygame.init()

        # Window creation.
        self.window = pygame.display.set_mode(
            (cons.WINDOW_SIZE, cons.WINDOW_SIZE))
        pygame.display.set_caption("Mac Gyver")

        # Maze setting.
        self.maze = Maze(cons.MAZE)
        self.maze.initialize_maze()
        self.maze.display(self.window)

        # MacGyver setting.
        self.mc_gyver = Player(cons.IMAGE_MG)
        self.mc_gyver.show(self.window)

        # objects setting.
        self.ether = Item(cons.IMAGE_ETHER)
        self.ether.position = self.ether.init_position(self.maze)
        self.ether.show(self.window)
        self.needle = Item(cons.IMAGE_NEEDLE)
        self.needle.position = self.needle.init_position(self.maze)
        self.needle.show(self.window)
        self.plastic_pipe = Item(cons.IMAGE_PLASTIC_PIPE)
        self.plastic_pipe.position = self.plastic_pipe.init_position(self.maze)
        self.plastic_pipe.show(self.window)
        self.syringe = Item(cons.IMAGE_SYRINGE)

        # Screen refresh.
        pygame.display.flip()

    def run(self):
        """Function containing the main loop of the game."""

        # Cont setting true (to continue).
        cont = 1
        # Keeping the window opened until event QUIT happens
        # (Alt + F4 or close cross), or until the maze is finished.
        while cont:
            # Saving processor resources.
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # If event QUIT, we go out of the while loop.
                if event.type == pygame.locals.QUIT:
                    cont = 0
                # What happens if user press a key down.
                elif event.type == pygame.locals.KEYDOWN:
                    ek = event.key
                    self.handle_move(ek)

                # Mac Gyver picked one of the objects.
                if self.mc_gyver.position == self.ether.position:
                    self.ether.exists = 0
                elif self.mc_gyver.position == self.needle.position:
                    self.needle.exists = 0
                elif self.mc_gyver.position == self.plastic_pipe.position:
                    self.plastic_pipe.exists = 0

                # Re-pasting after the event loop.
                self.maze.display(self.window)
                self.mc_gyver.show(self.window)

                # Checking if we can make the syringe.
                if (self.ether.exists == 0 and
                        self.needle.exists == 0 and
                        self.plastic_pipe.exists == 0):
                    self.syringe.exists = 1

                # If not, displaying the remaining objects.
                else:
                    if self.ether.exists:  # Not picked by Mac Gyver.
                        self.ether.show(self.window)
                    if self.needle.exists:  # Not picked by Mac Gyver.
                        self.needle.show(self.window)
                    if self.plastic_pipe.exists:  # Not picked by Mac Gyver.
                        self.plastic_pipe.show(self.window)

                # Screen refresh.
                pygame.display.flip()

                # When Mac Gyver arrives to the guard position (sprite "a").
                arrived_x = self.mc_gyver.sprite_x
                arrived_y = self.mc_gyver.sprite_y
                if self.maze.structure[arrived_x][arrived_y] == "a":
                    cont = self.arrival()

        # Closes the window.
        pygame.quit()

    def arrival(self):
        """Function to check
        if the player has collected every object needed,
        and prompt the end of game message.

        """

        # We check if there are still objects to pick in the maze
        if self.syringe.exists == 0:
            self.maze.text_display(self.window, cons.LOSTXT)
        # If not, the player has won.
        else:
            self.maze.text_display(self.window, cons.WINTXT)
        # We go out of the While loop.
        return 0

    def handle_move(self, ek):
        """Function to call the player's move function
        when a cursor movement key has been pressed.

        :param ek: event.key from pygame.event.get()

        """

        # If down cursor movement key.
        if ek == pygame.locals.K_DOWN:
            # Mg goes down for 1 sprite.
            self.mc_gyver.position = self.mc_gyver.move(
                'down', self.maze)
        # Up.
        elif ek == pygame.locals.K_UP:
            self.mc_gyver.position = self.mc_gyver.move(
                'up', self.maze)
        # Right.
        elif ek == pygame.locals.K_RIGHT:
            self.mc_gyver.position = self.mc_gyver.move(
                'right', self.maze)
        # Left.
        elif ek == pygame.locals.K_LEFT:
            self.mc_gyver.position = self.mc_gyver.move(
                'left', self.maze)

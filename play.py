#! /usr/bin env python3
# coding: utf-8

"""File containing the class Run, used to initialise the elements of the maze and run the loop playing the game."""

import pygame.locals
from maze import Maze
from items import Player
from items import Collected
import cons


class Run(object):
    """Class used to initialize the elements of the maze and run the loop playing the game."""

    def __init__(self):

        # Library initialization.
        pygame.init()

        # Window creation.
        self.window = pygame.display.set_mode((cons.WINDOW_SIZE, cons.WINDOW_SIZE))
        pygame.display.set_caption("Mac Gyver")

        # Maze setting.
        self.maze = Maze(cons.MAZE)
        self.maze.initialize_maze()
        self.maze.display(self.window)

        # Mac Giver setting.
        self.mc_giver = Player(cons.IMAGE_MG)
        self.mc_giver.show(self.window)

        # objects setting.
        self.ether = Collected(cons.IMAGE_ETHER)
        self.ether.position = self.ether.init_position(self.maze)
        self.ether.show(self.window)
        self.needle = Collected(cons.IMAGE_NEEDLE)
        self.needle.position = self.needle.init_position(self.maze)
        self.needle.show(self.window)
        self.plastic_pipe = Collected(cons.IMAGE_PLASTIC_PIPE)
        self.plastic_pipe.position = self.plastic_pipe.init_position(self.maze)
        self.plastic_pipe.show(self.window)
        self.syringe = Collected(cons.IMAGE_SYRINGE)

        # Screen refresh.
        pygame.display.flip()

    def run(self):
        """Function containing the main loop of the game."""

        # Cont setting true (to continue).
        cont = 1
        # Keeping the window opened until event QUIT happens (Alt + F4 or close cross), or until the maze is finished.
        while cont:
            pygame.time.Clock().tick(30)  # Saving processor resources.
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:  # If event QUIT, we go out of the while loop.
                    cont = 0
                elif event.type == pygame.locals.KEYDOWN:  # What happens if user press a key down.
                    if event.key == pygame.locals.K_DOWN:  # If down cursor movement key.
                        self.mc_giver.position = self.mc_giver.move('down', self.maze)  # Mg goes down for 1 sprite.
                    elif event.key == pygame.locals.K_UP:  # If up cursor movement key.
                        self.mc_giver.position = self.mc_giver.move('up', self.maze)  # Mg goes up for 1 sprite.
                    elif event.key == pygame.locals.K_RIGHT:  # If right cursor movement key.
                        self.mc_giver.position = self.mc_giver.move('right', self.maze)  # Mg goes right for 1 sprite.
                    elif event.key == pygame.locals.K_LEFT:  # If left cursor movement key.
                        self.mc_giver.position = self.mc_giver.move('left', self.maze)  # Mg goes left for 1 sprite.

                if self.mc_giver.position == self.ether.position:  # Mac Gyver picked the ether.
                    self.ether.exists = 0

                elif self.mc_giver.position == self.needle.position:  # Mac Gyver picked the needle.
                    self.needle.exists = 0
                elif self.mc_giver.position == self.plastic_pipe.position:  # Mac Gyver picked the plastic pipe.
                    self.plastic_pipe.exists = 0

                # Re-pasting after the event loop.
                self.maze.display(self.window)
                self.mc_giver.show(self.window)

                # Checking if we can make the syringe.
                if self.ether.exists == 0 and self.needle.exists == 0 and self.plastic_pipe.exists == 0:
                    self.syringe.exists = 1

                # If not, displaying the objects Mac Gyver still has to collect.
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
                if self.maze.structure[self.mc_giver.sprite_y][self.mc_giver.sprite_x] == "a":
                    # We check if there are still objects to pick in the maze
                    if self.syringe.exists == 0:
                        self.maze.text_display(self.window, "Vous vous êtes présenté devant \n"
                                               "le garde sans les armes \n"
                                               "nécessaires... \n"
                                               "vous avez perdu !")
                    # If not, the player has won.
                    else:
                        self.maze.text_display(self.window, "Bravo ! \n"
                                               "À l'aide de la seringue \n"
                                               "que vous avez fabriquée, \n"
                                               "vous avez vaincu le garde, \n"
                                               "vous vous échapez !")

                    # We go out of the While loop.
                    cont = 0

        # Closes the window.
        pygame.quit()

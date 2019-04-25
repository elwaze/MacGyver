#! /usr/bin env python3
# coding: utf-8


"""
Mac Giver game :
Game where the player has to move Mac Giver through a maze with the cursor movement keys.
Before trying to escape, he has to collect 3 objects on his way.

Python script.
files : main.py, maze.py, items.py, cons.py, maze.txt, images, font
"""


# Modules importation.
import pygame
import pygame.locals
import cons
from maze import Maze
from items import Player
from items import Collected


def main():

    # Library initialization.
    pygame.init()

    # Window creation.
    window = pygame.display.set_mode((cons.WINDOW_SIZE, cons.WINDOW_SIZE))
    pygame.display.set_caption("Mac Gyver")

    # Maze setting.
    maze = Maze(cons.MAZE)
    maze.initialize_maze()
    maze.display(window)

    # Mac Giver setting.
    mc_giver = Player(cons.IMAGE_MG)
    mc_giver.show(window)

    # objects setting.
    ether = Collected(cons.IMAGE_ETHER)
    ether.position = ether.init_position(maze)
    ether.show(window)
    needle = Collected(cons.IMAGE_NEEDLE)
    needle.position = needle.init_position(maze)
    needle.show(window)
    plastic_pipe = Collected(cons.IMAGE_PLASTIC_PIPE)
    plastic_pipe.position = plastic_pipe.init_position(maze)
    plastic_pipe.show(window)
    syringe = Collected(cons.IMAGE_SYRINGE)

    # Screen refresh.
    pygame.display.flip()

    # Cont setting true (to continue).
    cont = 1

    # display of the end of the game
    def text_display(text):
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

    # Keeping the window opened until event QUIT happens (Alt + F4 or close cross), or until the maze is finished.
    while cont:
        pygame.time.Clock().tick(30)  # Saving processor resources.
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:  # If event QUIT, we go out of the while loop.
                cont = 0
            elif event.type == pygame.locals.KEYDOWN:  # What happens if user press a key down.
                if event.key == pygame.locals.K_DOWN:  # If down cursor movement key.
                    mc_giver.position = mc_giver.move('down', maze)  # Mg goes down for 1 sprite.
                elif event.key == pygame.locals.K_UP:  # If up cursor movement key.
                    mc_giver.position = mc_giver.move('up', maze)  # Mg goes up for 1 sprite.
                elif event.key == pygame.locals.K_RIGHT:  # If right cursor movement key.
                    mc_giver.position = mc_giver.move('right', maze)  # Mg goes right for 1 sprite.
                elif event.key == pygame.locals.K_LEFT:  # If left cursor movement key.
                    mc_giver.position = mc_giver.move('left', maze)  # Mg goes left for 1 sprite.

            if mc_giver.position == ether.position:  # Mac Gyver picked the ether.
                ether.exists = 0

            elif mc_giver.position == needle.position:  # Mac Gyver picked the needle.
                needle.exists = 0
            elif mc_giver.position == plastic_pipe.position:  # Mac Gyver picked the plastic pipe.
                plastic_pipe.exists = 0

            # Re-pasting after the event loop.
            maze.display(window)
            mc_giver.show(window)

            # Checking if we can make the syringe.
            if ether.exists == 0 and needle.exists == 0 and plastic_pipe.exists == 0:
                syringe.exists = 1

            # If not, displaying the objects Mac Gyver still has to collect.
            else:
                if ether.exists:  # Not picked by Mac Gyver.
                    ether.show(window)
                if needle.exists:  # Not picked by Mac Gyver.
                    needle.show(window)
                if plastic_pipe.exists:  # Not picked by Mac Gyver.
                    plastic_pipe.show(window)

            # Screen refresh.
            pygame.display.flip()

            # When Mac Gyver arrives to the guard position (sprite "a").
            if maze.structure[mc_giver.sprite_y][mc_giver.sprite_x] == "a":
                # We check if there are still objects to pick in the maze
                if syringe.exists == 0:
                    text_display("Vous vous êtes présenté devant \n" 
                                 "le garde sans les armes \n"
                                 "nécessaires... \n"
                                 "vous avez perdu !")
                # If not, the player has won.
                else:
                    text_display("Bravo ! \n"
                                 "À l'aide de la seringue \n"
                                 "que vous avez fabriquée, \n"
                                 "vous avez vaincu le garde, \n"
                                 "vous vous échapez !")

                # We go out of the While loop.
                cont = 0

    # Closes the window.
    pygame.quit()


if __name__ == '__main__':
    import sys
    sys.exit(main())

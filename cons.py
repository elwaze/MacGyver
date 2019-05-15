#! /usr/bin env python3
# coding: utf-8


"""MacGyver.py constants."""

# Window parameters.
SIZE_IN_SPRITES = 15
SPRITE_SIZE = 35
WINDOW_SIZE = SIZE_IN_SPRITES * SPRITE_SIZE

# Maze file.
MAZE = "resources/maze.txt"

# Images.
IMAGE_WALL = "resources/images/wall.png"
IMAGE_BACKGROUND = "resources/images/background.png"
IMAGE_GUARD = "resources/images/guard.png"
IMAGE_MG = "resources/images/mg.png"
IMAGE_PLASTIC_PIPE = "resources/images/plastic_pipe.png"
IMAGE_NEEDLE = "resources/images/needle.png"
IMAGE_ETHER = "resources/images/ether.png"
IMAGE_SYRINGE = "resources/images/syringe.png"

# Font.
FONT = "resources/font/font.otf"

# Texts.

LOSTXT = "You've not assembled the syringe\n"\
         "to asleep the guard,\n"\
         " you're dead !!!"
WINTXT = "Well done !\n"\
         "With the 3 objects that you have\n"\
         " assembled, you asleep the guard and\n"\
         " you escape yourself !"

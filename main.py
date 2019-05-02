#! /usr/bin env python3
# coding: utf-8


"""
Mac Giver game :
Game where the player has to move Mac Giver through a maze with the cursor movement keys.
Before trying to escape, he has to collect 3 objects on his way.

Python script.
files : main.py, play.py, maze.py, items.py, cons.py, maze.txt, images, font
"""


# Modules importation.

from play import Run


def main():
    """Main function calling Run to run the game."""

    init = Run()

    return Run.run(init)


if __name__ == '__main__':
    import sys
    sys.exit(main())

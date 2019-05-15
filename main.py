#! /usr/bin env python3
# coding: utf-8


"""
MacGyver game:
Game where the player has to move MacGyver through a maze
with the cursor movement keys.
Before trying to escape, he has to collect 3 objects on his way.

Python script.
files: main.py, runner.py, maze.py, items.py, cons.py,
resources (maze.txt, images, font)

"""


# Modules importation.

from runner import Runner


def main():
    """Main function calling Runner to run the game."""

    runner = Runner()

    return runner.run()


if __name__ == '__main__':
    import sys
    sys.exit(main())

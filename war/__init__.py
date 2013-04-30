"""
Parses and validates inputs and instantiates a random game of War.
"""

from war import War


def main():
    w = War()
    winning_player = w.play(verbose=True)
    print "{0} won!".format(winning_player.name)

if __name__ == '__main__':
    main()

"""
Parses and validates inputs and instantiates a random game of War.
"""

import argparse

from war import War


def main():
    parser = argparse.ArgumentParser(description='Play a game of War.')
    parser.add_argument('--players', type=int, nargs='?', required=True,
                        help='a count of players')
    parser.add_argument('--suits', type=int, nargs='?', required=True,
                        help='a count of suits')
    parser.add_argument('--ranks', type=int, nargs='?', required=True,
                        help='a count of ranks')
    parser.add_argument("--verbose", help="show game in progress",
                        action="store_true")
    parser.add_argument("--slow", help='wait for a second between turns',
                        action="store_true")
    args = parser.parse_args()

    w = War(count_of_players=args.players, count_of_suits=args.suits,
            count_of_ranks=args.ranks)
    winning_player = w.play(verbose=args.verbose, slow=args.slow)

    print "Winner: {0}".format(winning_player.name)

if __name__ == '__main__':
    main()

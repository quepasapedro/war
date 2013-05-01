from player import Player
from deck import Deck


class War:
    """
    Encapsulates the logic which drives the game of War.
    """

    def __init__(self, count_of_players, count_of_suits, count_of_ranks):
        """
        Sets up deck and players.
        """

        # TODO: Raise ValueError for invalid counts (e.g., 0, 1)
        # TODO: Allow inputing names

        self.players = []
        for n in range(count_of_players):
            self.players.append(Player(name="Player {0}".format(str(n + 1))))

        self.deck = Deck(count_of_suits=count_of_suits,
                         count_of_ranks=count_of_ranks)
        self.deck.shuffle()
        self.deck.deal(self.players)

    def play(self, verbose=False):
        """
        Plays a random game of war and returns the player object which
        wins the game.
        """

        return self.players[0] # XXX return actual winner

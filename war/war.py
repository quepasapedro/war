from .player import Player
from .deck import Deck


class War:
    """
    Encapsulates the logic which drives the game of War.
    """

    def __init__(self, count_of_suits, count_of_ranks, count_of_players):
        """
        Sets up deck and players.
        """

        # TODO: Raise ValueError for specific invalid numbers, names
        # TODO: Allow inputing names

        self.deck = Deck(count_of_suits=count_of_suits,
                         count_of_players=count_of_players)
        self.deck.shuffle()

        self.players = []
        for n in range(count_of_players):
            self.players.append(Player(name=str(n + 1)))

    def play(self, verbose=False):
        """
        Plays a random game of war and returns the player object which
        wins the game.
        """

        self.deck.deal(self.players)

    def battle(self):
        pass

    def war(self):
        pass

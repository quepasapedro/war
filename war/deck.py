import random
import collections

from .card import Card


class Deck(collections.deque):
    """
    Represents a deck of playing cards, based on Python's set type. The
    number cards in the deck equals the count of suits times the count
    of ranks. Defaults to four suits and thirteen ranks (a standard
    French-style deck of fifty-two cards).
    """

    def __init__(self, s=[], count_of_suits=4, count_of_ranks=13):
        """
        Creates a full set of playing cards, with exactly one each for
        each combination of suit and rank until the counts provided to
        the constructor are satisfied. For example, four suits and
        thirteen ranks will cause fifty-two cards to be created. Before
        shuffle() is called, guaranteed to be in order.

        Equivalent to the `create` method of the original exercise
        interface.
        """

        # allows me to init a deck by hand or let it init automatically
        if s:
            super(Deck, self).__init__(s)
        else:
            self.count_of_suits = count_of_suits
            self.count_of_ranks = count_of_ranks

            if count_of_suits == 1 and count_of_ranks == 1:
                raise ValueError("Cannot have a deck of one card!")

            for suit in range(count_of_suits):
                for rank in range(count_of_ranks):
                    self.append(Card(suit, rank))

    def shuffle(self):
        """
        Randomize the position of the Card objects in place.
        """
        cards = list(self)
        random.shuffle(cards)
        self.clear()
        self.extend(cards)

    def deal(self, players=[]):
        """
        Deal out Card objects to each of the players until all cards are
        distributed from the top of the Deck (which itself is a FIFO
        stack). The deck will be empty after this method returns.
        """

        # TODO: What if the number of cards aren't divisible by the
        # number of players?

        if players == []:
            raise ValueError("No players for dealing")

        for card_index in range(len(self)):
            player_index = card_index % len(players)
            players[player_index].take_card(self.pop())

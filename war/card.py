class Card(object):
    """
    Represents a French-style playing card with arbitrary rank and suit.
    This type is comparable to itself only.
    """

    # TODO: Raise ValueError if comparing against other types or better
    # handle other types to allow Card-to-int comparison

    def __init__(self, suit=1, rank=1):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __repr__(self):
        return 'card.suit == {0}, card.rank == {1}'.format(self.suit,
                                                           self.rank)

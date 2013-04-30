class Player:
    """
    Represents an agent in the game of War. Remembers hand and name.
    """

    def __init__(self, name="Alice", hand=None):
        self.name = name
        if hand:
            self.hand = hand
        else:
            self.hand = []

    def take_card(self, card):
        """
        Accept a card when given to the top of the hand, which is a FIFO
        stack.
        """

        # TODO: Validate Card object

        self.hand.append(card)

    def take_cards(self, cards):
        """
        Accept a sequence of cards.
        """

        # TODO: Validate Card objects and sequence

        self.hand.extend(cards)

    def play_card(self):
        """
        Return the top card from the hand, which is a FIFO stack.
        """

        return self.hand.pop()

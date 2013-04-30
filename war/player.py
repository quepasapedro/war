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

        self.hand.append(card)

    def play_card(self):
        """
        Return the top card from the hand, which is a FIFO stack.
        """

        return self.hand.pop()

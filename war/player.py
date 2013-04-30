class Player:
    """
    Represents an agent in the game of War.
    """

    def __init__(self, name="Alice", hand=[]):
        self.hand = hand

    def take_card(self, card):
        self.hand.append(card)

    def play_card(self):
        self.hand.pop()

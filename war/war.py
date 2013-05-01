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

        self.players = {}
        for n in range(count_of_players):
            p = Player(name="Player {0}".format(str(n + 1)))
            self.players[id(p)] = p

        self.deck = Deck(count_of_suits=count_of_suits,
                         count_of_ranks=count_of_ranks)
        self.deck.shuffle()
        self.deck.deal(self.players.values())

    def play(self, verbose=False):
        """
        Plays a random game of war and returns the player object which
        wins the game.
        """

        while True:
            self.pot = []
            battle = {}
            for player in self.players.itervalues():
                if len(player.hand) > 0:
                    battle[id(player)] = player.play_card()
            battle_winner = self.battle(battle)
            battle_winner.take_cards(self.pot)

            # print the outcome
            war_winner = self.get_winner()
            if war_winner:
                return war_winner
            elif verbose:
                status = ''
                for player in self.players.itervalues():
                    status += '*' * len(player.hand) + ' '
                print status

    def battle(self, battle={}):
        """
        Accepts a hash of players with the cards they play. Recursively
        calls itself until there is a single definitive winner, which
        it returns. Accumulates cards played in the pot for each call.
        """

        high_card = max(battle.values(), key=lambda c: c.rank)
        battle_winners = []
        for player_id, card in battle.iteritems():
            if card == high_card:
                battle_winners.append(self.players[player_id])

        self.pot.extend(battle.values())

        if len(battle_winners) == 1:
            return battle_winners[0]
        else:
            next_battle = {}
            for player in battle_winners:
                if len(player.hand) > 0:
                    # another card face down ...
                    self.pot.extend(player.play_card())
                    # ... and another card face up
                    next_battle[id(player)] = player.play_card()
            return self.battle(next_battle)

    def get_winner(self):
        """
        Returns the player object which has all the cards. If no winner
        is found, it returns None.
        """

        for player in self.players.itervalues():
            if self.deck.count_of_cards == len(player.hand):
                return player

        return None

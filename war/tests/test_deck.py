import unittest
import collections
import copy

from war.deck import Deck
from war.player import Player


class TestDeck(unittest.TestCase):
    def test_deck_can_work_like_a_deque(self):
        self.assertEqual(Deck([1, 2, 3]), collections.deque([1, 2, 3]))

    def test_deck_lets_me_set_rank_and_suit_counts_in_constructor(self):
        d = Deck(count_of_suits=2, count_of_ranks=2)
        self.assertEqual(d.count_of_suits, 2)
        self.assertEqual(d.count_of_ranks, 2)

        d = Deck(count_of_suits=4, count_of_ranks=4)
        self.assertEqual(d.count_of_suits, 4)
        self.assertEqual(d.count_of_ranks, 4)

    def test_deck_remembers_its_own_starting_count(self):
        d = Deck(count_of_suits=2, count_of_ranks=2)
        self.assertEqual(d.count_of_cards, 4)
        self.assertEqual(d.count_of_cards, len(d))

        d.shuffle()
        self.assertEqual(d.count_of_cards, 4)
        self.assertEqual(d.count_of_cards, len(d))

        d.deal([Player(), Player()])
        self.assertEqual(d.count_of_cards, 4)
        self.assertNotEqual(d.count_of_cards, len(d))

    def test_deck_shuffle_works_and_is_non_destructive(self):
        deck = Deck()
        control = collections.deque(deck)
        self.assertEqual(len(deck), len(control))
        self.assertEqual(deck, control)

        # same number of items in different order
        deck.shuffle()
        self.assertEqual(len(deck), len(control))
        self.assertNotEqual(deck, control)

        # make a shallow copy
        another_deck = copy.copy(deck)
        self.assertEqual(len(deck), len(another_deck))
        self.assertEqual(deck, another_deck)

        # shuffle shallow copy doesn't match control or other
        another_deck.shuffle()
        self.assertEqual(len(deck), len(another_deck))
        self.assertEqual(len(deck), len(control))
        self.assertNotEqual(deck, another_deck)
        self.assertNotEqual(deck, control)

    def test_does_not_allow_deck_of_one_card(self):
        # two cards is fine
        Deck(count_of_suits=2, count_of_ranks=1)
        Deck(count_of_suits=1, count_of_ranks=2)

        # but one card makes no sense for War
        with self.assertRaises(ValueError):
            Deck(count_of_suits=1, count_of_ranks=1)

    def test_deck_deals_out_to_two_players_correctly(self):
        players = []
        for n in range(2):                              # 2 players
            players.append(Player(name=str(n + 1)))

        d = Deck(count_of_suits=4, count_of_ranks=4)    # 16 cards
        d.shuffle()
        d.deal(players)

        # 8 cards each ...
        self.assertEqual(len(players[0].hand), 8)
        self.assertEqual(len(players[0].hand), len(players[1].hand))

        # ... of different cards
        for n in range(len(players[0].hand)):
            self.assertNotEqual(players[0].hand[n].__hash__(),
                                players[1].hand[n].__hash__())

    def test_deck_deals_out_to_three_players_correctly(self):
        players = []
        for n in range(3):                              # 3 players
            players.append(Player(name=str(n + 1)))

        d = Deck(count_of_suits=4, count_of_ranks=9)    # 36 cards
        d.shuffle()
        d.deal(players)

        # 12 cards each ...
        self.assertEqual(len(players[0].hand), 12)
        self.assertEqual(len(players[0].hand), len(players[1].hand))
        self.assertEqual(len(players[1].hand), len(players[2].hand))

        # ... of different cards
        for n in range(len(players[0].hand)):
            self.assertNotEqual(players[0].hand[n].__hash__(),
                                players[1].hand[n].__hash__())
            self.assertNotEqual(players[1].hand[n].__hash__(),
                                players[2].hand[n].__hash__())

    def test_deck_deals_out_to_four_players_correctly(self):
        players = []
        for n in range(4):                              # 4 players
            players.append(Player(name=str(n + 1)))

        d = Deck(count_of_suits=8, count_of_ranks=8)    # 64 cards
        d.shuffle()
        d.deal(players)

        # 16 cards each ...
        self.assertEqual(len(players[0].hand), 16)
        self.assertEqual(len(players[0].hand), len(players[1].hand))
        self.assertEqual(len(players[1].hand), len(players[2].hand))
        self.assertEqual(len(players[2].hand), len(players[3].hand))

        # ... of different cards
        for n in range(len(players[0].hand)):
            self.assertNotEqual(players[0].hand[n].__hash__(),
                                players[1].hand[n].__hash__())
            self.assertNotEqual(players[1].hand[n].__hash__(),
                                players[2].hand[n].__hash__())
            self.assertNotEqual(players[2].hand[n].__hash__(),
                                players[3].hand[n].__hash__())

    # TODO: Tests with uneven numbers of cards
    # TODO: Test to make sure cards do not recur in others' hands

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

    def test_deck_deals_out_to_two_players_in_sequence_by_cards(self):
        players = []
        for n in range(2):
            players.append(Player(name=str(n + 1)))
        d = Deck(count_of_suits=4, count_of_ranks=4)
        d.shuffle()
        d.deal(players)

        self.assertEqual(len(players[0].hand), len(players[1].hand))
        self.assertEqual(len(players[0].hand), 8)

        for n in range(len(players[0].hand)):
            self.assertNotEqual(players[0].hand[n].__hash__(),
                                players[1].hand[n].__hash__())

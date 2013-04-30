import unittest
from collections import deque
from copy import copy

from war.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_can_work_like_a_deque(self):
        self.assertEqual(Deck([1, 2, 3]), deque([1, 2, 3]))

    def test_deck_lets_me_set_rank_and_suit_counts_in_constructor(self):
        d = Deck(count_of_suits=2, count_of_ranks=2)
        self.assertEqual(d.count_of_suits, 2)
        self.assertEqual(d.count_of_ranks, 2)

        d = Deck(count_of_suits=4, count_of_ranks=4)
        self.assertEqual(d.count_of_suits, 4)
        self.assertEqual(d.count_of_ranks, 4)

    def test_deck_shuffle_works_and_is_non_destructive(self):
        deck = Deck()
        control = deque(deck)
        self.assertEqual(len(deck), len(control))
        self.assertEqual(deck, control)

        # same number of items in different order
        deck.shuffle()
        self.assertEqual(len(deck), len(control))
        self.assertNotEqual(deck, control)

        # make a shallow copy
        another_deck = copy(deck)
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

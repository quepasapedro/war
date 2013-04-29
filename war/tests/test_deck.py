import unittest
from collections import deque
from war.deck import Deck


class TestDeck(unittest.TestCase):
    # def setUp(self):
    #     pass

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
        d = Deck()
        control = deque(d)
        self.assertEqual(len(d), len(control))
        self.assertEqual(d, control)

        # same number of items in different order --
        # XXX for very small decks, odds increase this may fail if the
        # random permutation matches the original order; for very large
        # decks, performance may suffer
        d.shuffle()
        self.assertEqual(len(d), len(control))
        self.assertNotEqual(d, control)

    def test_does_not_allow_deck_of_one_card(self):
        # two cards is fine
        Deck(count_of_suits=2, count_of_ranks=1)
        Deck(count_of_suits=1, count_of_ranks=2)

        # but one card makes no sense for War
        with self.assertRaises(ValueError):
            Deck(count_of_suits=1, count_of_ranks=1)

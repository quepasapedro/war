import unittest
from war.card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.control = Card(rank=1, suit=1)
        self.tying_rank_same_suit = Card(rank=1, suit=1)
        self.tying_rank_different_suit = Card(rank=1, suit=2)

    def test_card_ranks_cause_tie_equal_irrespective_of_suit(self):
        self.assertEqual(self.control, self.tying_rank_same_suit)
        self.assertEqual(self.control, self.tying_rank_different_suit)

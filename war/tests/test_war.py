import unittest

from war.war import War


class TestWar(unittest.TestCase):
    def test_war_get_winner(self):
        w = War()

        p1 = w.players.itervalues().next()
        p1.hand = []  # clear out this player's hand

        # so the remaining player must win...
        self.assertEqual(w.get_winner(), w.players.itervalues().next())

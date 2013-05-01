import unittest

from war.war import War
from war.player import Player


class TestWar(unittest.TestCase):
    def test_war_get_winner(self):
        w = War()

        p1 = w.players.itervalues().next()
        p1.hand = []  # clear out this player's hand

        # so the remaining player must win...
        self.assertEqual(w.get_winner(), w.players.itervalues().next())

    def test_war_plays_game_without_failing_and_returns_a_winner(self):
        w = War()
        assert isinstance(w.play(), Player)

    # TODO: test for infinite recursion edge cases in War.battle()
    # TODO: test for init cases which should raise exceptions

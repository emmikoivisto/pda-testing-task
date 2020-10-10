import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.test_card1 = Card("Heart", 1)
        self.test_card2 = Card("Diamonds", 10)
        self.card_game = CardGame()

    def test_card_has_suit(self):
        self.assertEqual("Heart", self.test_card1.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.test_card1.value)

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.test_card1))

    def test_highest_card(self):
        self.assertEqual(self.test_card2, self.card_game.highest_card(self.test_card1, self.test_card2))
        
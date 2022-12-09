import unittest
import Player
import Card
import Deck
import random

class TestCardsExercice1(unittest.TestCase):
    def test_card_constructor(self):
        self.assertTrue(isinstance(Card.Card('coeur', 12), Card.Card))

    def test_cards_equal_value(self):
        ace_of_hearts = Card.Card('coeur', 12)
        ace_of_spades = Card.Card('pique', 12)
        self.assertEqual(ace_of_hearts.getNumber(), ace_of_spades.getNumber(), 'Two cards having '
                                                       'same value should be considered equal')

    def test_cards_comparison(self):
        ace_of_hearts = Card.Card('coeur', 12)
        two_of_hearts = Card.Card('coeur', 13)
        five_of_hearts = Card.Card('coeur', 5)

        self.assertTrue(ace_of_hearts.getNumber() > five_of_hearts.getNumber())
        self.assertTrue(two_of_hearts.getNumber() > ace_of_hearts.getNumber() > five_of_hearts.getNumber(),
                        'The two card is the highest card')
        self.assertTrue(five_of_hearts.getNumber() < two_of_hearts.getNumber(),
                        'The two card is the highest card')

class TestDeckExercice1(unittest.TestCase):
     def test_deck_has_52_cards(self):
         deck = Deck.Deck()
         self.assertEqual(len(deck.getCards()), 52, 'The president is a card game '
                                               'requiring 52 cards')
     def test_deck_shuffling(self):
         deck_1 = Deck.Deck()
         deck_2 = Deck.Deck()
         self.assertEqual(deck_1.getCards(), deck_2.getCards(), 'A new deck should not be automatically shuffled')
         deck_2.shuffle()
         self.assertNotEqual(deck_1.getCards(), random.shuffle(deck_2.getCards()),'Shuffling a deck '
                                                        'randomizes the '
                                                        'cards order')


if __name__ == '__main__':
    unittest.main()

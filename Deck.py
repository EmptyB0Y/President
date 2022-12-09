import Card
import random

class Deck:

    _cards = []

    def __init__(self) -> None:
        for i in range(1,53):
            if(i <= 13):
                crd = Card.Card("carreau",i)
                self._cards.append(crd)
            elif(i <= 26):
                crd = Card.Card("coeur",i-13)
                self._cards.append(crd)
            elif(i <= 39):
                crd = Card.Card("trefle",i-26)
                self._cards.append(crd)
            elif(i <= 52):
                crd = Card.Card("pique",i-39)
                self._cards.append(crd)

    def shuffle(self):
        random.shuffle(self._cards)

    def getCards(self):
        deck = []
        for i in self._cards:
            deck.append(i.__str__())
        return deck
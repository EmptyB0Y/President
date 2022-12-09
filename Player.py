import Card
import random

class Player:

  
    _role = ""

    def __init__(self,name='') -> None:
        self._name = name
        if(self._name == ''):
            self._name = str(random.randbytes(7))
        self._deck = list()
    
    def getRole(self):
        return self._role
    
    def setRole(self,role):
        self._role = role

    def addCard(self,crd):
        self._deck.append(crd)
    
    def drawCards(self,crd_lst):
        for i in crd_lst:
            self._deck.remove(i)

    def getName(self):
        return self._name

    def getDeck(self):
        return self._deck

    def getDeckOrganized(self) -> dict:
        organized = {}
        for i in range(1,14):
            create = True
            for j in self._deck:
                if(j.getNumber() == i):
                    if(create):
                        organized[i] = list()
                        create = False
                    organized[i].append(j.__str__())
        return organized

    def exchangeWithPresident(pl):
        pass

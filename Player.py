import Card

class Player:

  
    _role = ""

    def __init__(self,name) -> None:
        self._name = name  
        self._deck = list()
    
    def getRole(self):
        return self._role
    
    def setRole(self,role):
        self._role = role

    def addCard(self,crd):
        self._deck.append(crd)
    
    def drawCard(self,crd_lst):
        draw = list()
        for i in crd_lst:
            try:
                self._deck.remove(self._deck.index(i))
                draw.append(self._deck.index(i))
            except(ValueError):
                print(ValueError)
        return draw

    def getName(self):
        return self._name

    def getDeck(self):
        return self._deck
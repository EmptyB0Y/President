class Card:

    _color = ""
    _number = 0

    def __init__(self,color,number) -> None:
        self._color = color
        self._number = number

    def __str__(self) -> str:
        card_str = ""
        if self._color == "carreau":
                card_str = "♢"
        elif self._color == "coeur":
                card_str = "♡"
        elif self._color == "trefle":
                card_str = "♧"
        elif self._color == "pique":
                card_str = "♤"
        if self._number == 11:
            card_str += "J"
        elif self._number == 12:
            card_str += "Q"
        elif self._number == 13:
            card_str += "K"
        else:
            card_str += str(self._number)
        
        return card_str
             

    def getColor(self):
        return self._color

    def getNumber(self):
        return self._number


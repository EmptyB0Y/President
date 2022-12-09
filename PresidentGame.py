import Card
import Player
import random
import Deck

class PresidentGame():
    players = list()
    playing = True
    player_nbr = 0
    main_deck = [] #Deck.Deck()

    def __init__(self,playerList=[]) -> None:
        if(len(playerList) >= 3 and len(playerList) <= 6):
            for i in playerList:
                self.player_nbr += 1
                self.players.append(Player.Player(i))

    def makeDeck(self):
        while (self.player_nbr < 3 or self.player_nbr > 6):
            self.player_nbr = int(input("Player amount (between 3 and 6) : "))

        for i in range(1,53):
            if(i <= 13):
                crd = Card.Card("carreau",i)
                self.main_deck.append(crd)
            elif(i <= 26):
                crd = Card.Card("coeur",i-13)
                self.main_deck.append(crd)
            elif(i <= 39):
                crd = Card.Card("trefle",i-26)
                self.main_deck.append(crd)
            elif(i <= 52):
                crd = Card.Card("pique",i-39)
                self.main_deck.append(crd)

        random.shuffle(self.main_deck)

        if(self.players == []): 
            for i in range(1,self.player_nbr+1):
                name = input("Name for player " + str(i) + " : ")
                pl = Player.Player(name)
                self.players.append(pl)

        plcount = self.player_nbr-1

        while len(self.main_deck) > 0:
            if(plcount == -1):
                plcount = self.player_nbr-1

            card = self.main_deck.pop(0)
            self.players[plcount].addCard(card)            
            plcount -= 1

        self.main_deck.clear()

    def startGame(self):
        first_hand = None
        hand = {}
        playAgain = True
        index = 0

        while (self.playing):

            if(playAgain):
                playAgain = False
                for pl in self.players:
                    if(first_hand is None):
                        for i in pl.getDeck():
                            if(i.getColor() == "coeur" and i.getNumber() == 10):
                                first_hand = pl
                                break
                    elif(pl.getRole() == "president"):
                        first_hand = pl
                        for pl2 in self.players:
                            if(pl2.getRole() == "asswipe"):
                                pl2.exchangeWithPresident(pl)
                        

                print(first_hand.getName() + " has the upper hand !")
                startIndex = self.players.index(first_hand)

                hand = {}
            
            exit = False
            while(not exit):
                print("Your hand : "+str(self.players[startIndex].getDeckOrganized()))
                hand[self.players[startIndex]] = input("Your choice, "+self.players[startIndex].getName()+ " : ").split("-")
                cardsIndex = int(hand[self.players[startIndex]][0])
                cardNbr = int(hand[self.players[startIndex]][1])

                if(not self.players[startIndex].getDeckOrganized().keys().__contains__(cardsIndex)):
                    print("You don't have this card !")
                elif(len(self.players[startIndex].getDeckOrganized()[cardsIndex]) < cardNbr):
                    print("You can't play this amount of cards !")
                else:
                    exit = True

            count = 1
            cut = False
            if(int(hand[self.players[startIndex]][0]) == 13):
                cut = True

            index = startIndex
            stamp = startIndex
            while(count < self.player_nbr):
                if(index < self.player_nbr-1):
                    index += 1
                else:
                    index = 0
                #CHECK IF PLAYER CAN PLAY
                canPlay = False
                for j in self.players[index].getDeckOrganized().keys():
                    #check if card is present
                    if(j >= int(hand[self.players[startIndex]][0])):
                        #check if card is in enough amount
                        if(len(self.players[index].getDeckOrganized()[j]) >= int(hand[self.players[startIndex]][1]) and not cut):
                            canPlay = True

                if (canPlay):
                    print("Your hand : "+str(self.players[index].getDeckOrganized()))
                    #Syntax : indexOfCard-numberOfCards
                    #Skip turn by entering 0-0
                    exit = False
                    while(not exit):
                        hand[self.players[index]] = input("Your choice, "+self.players[index].getName()+ " : ").split("-")
                        cardsIndex = int(hand[self.players[index]][0])
                        cardNbr = int(hand[self.players[index]][1])
                        if(cardsIndex != '0' and cardNbr != '0'):
                            if(not self.players[index].getDeckOrganized().keys().__contains__(cardsIndex)):
                                print("You don't have this card, skip turn by typing 0-0 !")
                            elif(int(hand[self.players[startIndex]][1]) != cardNbr):
                                print("You can't play this amount of cards, skip turn by typing 0-0 !")
                            elif(int(hand[self.players[stamp]][0]) > cardsIndex):
                                print("You have to play an even or higher card than the previous player, skip turn by typing 0-0 !")
                            elif(len(self.players[index].getDeckOrganized()[cardsIndex]) < cardNbr):
                                print("You don't have enough cards, skip turn by typing 0-0 !")
                            else:
                                exit= True
                        else:
                            exit = True
                        
                    if(int(hand[self.players[index]][0]) == 13):
                        print("cut")
                        cut = True
                else:
                    print(str(self.players[index].getName()) + " can't play !")
                    hand[self.players[index]] = ['0','0']
                count += 1
                stamp = index

            #Check drawn hand
            for i in range(0,len(hand)):
                if(hand[self.players[i]][0] != "0" and hand[self.players[i]][1] != "0"):
                    cardsIndex = int(hand[self.players[i]][0])
                    cardNbr = int(hand[self.players[i]][1])

                    cards = self.players[i].getDeckOrganized()[cardsIndex]
                    drew = list()
                    drewStr = list()
                    for j in range(0,cardNbr):
                        for x in self.players[i].getDeck():
                            if(x.__str__() == cards[j]):
                                drew.append(x)
                                drewStr.append(x.__str__())

                    print(self.players[i].getName() + " played " + str(drew))
                    self.players[i].drawCards(drew)
                else:
                    print(self.players[i].getName() + " passed")

            #Check if a player has won
            biggestDeck = self.players[0]
            for pl in self.players:
                if(len(pl.getDeck()) == 0):
                    pl.setRole("president")
                    print(pl.getName() + " is the president")
                    self.playing = False
                elif(len(pl.getDeck()) > len(biggestDeck.getDeck())):
                    biggestDeck = pl

            if(not self.playing):
                biggestDeck.setRole("asswipe")
                print(pl.getName() + " is the asswipe")

                choice = None
                while(choice != 'y' or choice != 'n'):
                    choice = input("Play again ? : Y/n")

                if(choice == 'y'):
                    playAgain = True
                    self.playing = True
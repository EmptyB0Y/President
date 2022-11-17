import Card
import Player
import random

players = list()
playing = True
player_nbr = 0
main_deck = []

while (player_nbr < 3 or player_nbr > 6):
    player_nbr = int(input("Player amount (between 3 and 6) : "))

for i in range(1,53):
    if(i <= 13):
        crd = Card.Card("carreau",i)
        main_deck.append(crd)
    elif(i <= 26):
        crd = Card.Card("coeur",i-13)
        main_deck.append(crd)
    elif(i <= 39):
        crd = Card.Card("trefle",i-26)
        main_deck.append(crd)
    elif(i <= 52):
        crd = Card.Card("pique",i-39)
        main_deck.append(crd)

random.shuffle(main_deck)

for i in range(1,player_nbr+1):
    name = input("Name for player " + str(i) + " : ")
    pl = Player.Player(name)
    players.append(pl)

plcount = player_nbr-1

while len(main_deck) > 0:
    if(plcount == -1):
        plcount = player_nbr-1

    card = main_deck.pop(0)
    players[plcount].addCard(card)
    
    #print("added "+str(card)+" to "+players[plcount].getName()+"'s deck")
    plcount -= 1

main_deck.clear()

for pl in players:
    print(str(len(pl.getDeck())))

first_hand = None
hand = {}
playAgain = True
index = 0

while (playing):

    if(playAgain):
        playAgain = False
        for pl in players:
            if(first_hand is None):
                for i in pl.getDeck():
                    if(i.getColor() == "coeur" and i.getNumber() == 10):
                        first_hand = pl
                        break
            elif(pl.getRole() == "president"):
                first_hand = pl
                for pl2 in players:
                    if(pl2.getRole() == "asswipe"):
                        pl2.exchangeWithPresident(pl)
                

        print(first_hand.getName() + " has the upper hand !")
        startIndex = players.index(first_hand)

        hand = {}

    print("Your hand : "+str(players[startIndex].getDeckOrganized()))
    hand[players[startIndex]] = input("Your choice, "+players[startIndex].getName()+ " : ").split("-")
    index = startIndex

    count = 1
    cut = False
    if(int(hand[players[startIndex]][0]) == 13):
        cut = True

    while(count < player_nbr):
        if(index < player_nbr-1):
            index += 1
        else:
            index = 0
        #CHECK IF PLAYER CAN PLAY
        canPlay = False
        for j in players[index].getDeckOrganized().keys():
            #check if card is present
            if(j >= int(hand[players[startIndex]][0])):
                #check if card is in enough amount
                if(len(players[index].getDeckOrganized()[j]) >= len(hand[players[startIndex]][1]) and not cut):
                    canPlay = True

        if (canPlay):
            print("Your hand : "+str(players[index].getDeckOrganized()))
            hand[players[index]] = input("Your choice, "+players[index].getName()+ " : ").split("-")
            if(int(hand[players[index]][0]) == 13):
                print("cut")
                cut = True
        else:
            print(str(players[index].getName()) + " can't play !")
            hand[players[index]] = ['0','0']
        count += 1

    #Check drawn hand
    for i in range(0,len(hand)):
        if(hand[players[i]][0] != "0" and hand[players[i]][1] != "0"):
            cardsIndex = int(hand[players[i]][0])
            cardNbr = int(hand[players[i]][1])
            if(not players[i].getDeckOrganized().__contains__(cardsIndex)):
                print("error 1")
                #TODO ERROR
                #pass
            elif(cardNbr > len(players[i].getDeckOrganized()[cardsIndex]) or cardNbr > 4):
                print("error 2")
                #TODO ERROR
                #pass
            elif(cardNbr != len(hand[players[startIndex]][1])):
                print("error 3")
                #TODO ERROR
                #pass
            else:
                cards = players[i].getDeckOrganized()[cardsIndex]
                drew = list()
                for j in range(0,cardNbr):
                    for x in players[i].getDeck():
                        if(x.__str__() == cards[j]):
                            drew.append(x)
                    print(players[i].getName() + " played " + str(cards[j]))
                players[i].drawCards(drew)
                startIndex = i
        else:
            print(players[i].getName() + " passed")

    #Check if a player has won
    biggestDeck = players[0]
    for pl in players:
        if(len(pl.getDeck()) == 0):
            pl.setRole("president")
            print(pl.getName() + " is the president")
            playing = False
        elif(len(pl.getDeck()) > len(biggestDeck.getDeck())):
            biggestDeck = pl

    if(not playing):
        biggestDeck.setRole("asswipe")
        print(pl.getName() + " is the asswipe")

        choice = None
        while(choice != 'y' or choice != 'n'):
            choice = input("Play again ? : Y/n")

        if(choice == 'y'):
            playAgain = True
            playing = True


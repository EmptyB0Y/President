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

for pl in players:
    if(first_hand is None):
        for i in pl.getDeck():
            if(i.getColor() == "coeur" and i.getNumber() == 12):
                first_hand = pl
                break
    else:
        break

print(first_hand.getName() + " has the upper hand !")
startIndex = players.index(first_hand)

hand = {}
while (playing):
    print("Your hand : "+str(players[startIndex].getDeckOrganized()))
    hand[players[startIndex]] = input("Your choice, "+players[startIndex].getName()+ " : ").split("-")
    index = startIndex
    for i in range(0,player_nbr-1):
        if(index < player_nbr-1):
            index += 1
        else:
            index = 0
        #CHECK IF PLAYER CAN PLAY
        #FIXME
        canPlay = False
        for j in players[index].getDeckOrganized().keys():
            print(j)
            print(hand[players[startIndex]][0])
            if(j >= int(hand[players[startIndex]][0])):
                if(len(players[index].getDeckOrganized()[j]) >= len(players[startIndex].getDeckOrganized()[j])):
                    canPlay = True

        if (canPlay):
            print("test")
            print("Your hand : "+str(players[index].getDeckOrganized()))
            hand[players[index]] = input("Your choice, "+players[index].getName()+ " : ").split("-")
        else:
            print(str(players[index].getName()) + " can't play !")

    for i in range(0,len(hand)):
        cardsIndex = int(hand[players[i]][0])
        cardNbr = int(hand[players[i]][1])
        if(cardsIndex != "*" and cardNbr != "*"):
            if(not players[i].getDeckOrganized().__contains__(cardsIndex)):
                #TODO ERROR
                pass
            elif(cardNbr > len(players[i].getDeckOrganized()[cardsIndex]) or cardNbr > 4):
                #TODO ERROR
                pass
            elif(cardNbr != hand[players[startIndex]][1]):
                #TODO ERROR
                pass
            else:
                cards = players[i].getDeckOrganized()[cardsIndex]
                for j in range(0,cardNbr):
                    print(players[i].getName() + " played " + str(cards[j]))


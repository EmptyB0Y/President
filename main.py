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

print(first_hand.getName())
#while (playing):


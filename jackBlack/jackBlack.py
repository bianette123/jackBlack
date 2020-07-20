from deck import Deck
from player import Player
from player import Dealer
from player import Hand

p1 = Player('i-lo')
dealer = Dealer('Mr.jack')
deck = Deck()
deck.shuffle()

dealer.deal(p1,deck)
p1.hand.display()
print()
dealer.deal(dealer,deck)
dealer.hand.display()





#checking for ace value/in hand
#drewAce = False
#        for i in range(cNum):
#            topCard = deck.pop()
#            draw.append(topCard)
#            if topcard.rank == 'A':
#                drewAce = True

#        if not(player.hand.checkAce()) and drewAce:
#            print('you drew')
#            for card in player.hand.cards:
#                card.reveal()
#            for card in draw:
#                card.reveal()
#            print("High or low?")
#            aceValue = input()
#        else:
#            aceValue = False

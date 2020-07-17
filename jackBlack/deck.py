from card import Card
import random as rand 


class Deck :
    ''' class that describes a deck of cards '''

    def __init__(self):
        self.generateDeck()
        self.cardNum = len(self.cards)

    
    def generateDeck(self):
        ranks = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['spades','cloves','hearts','dimonds']
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit = suit,rank = rank))

    def shuffle(self):
        self.cards = rand.sample(self.cards,len(self.cards))

    def display(self):
        for card in self.cards :
            card.reveal()








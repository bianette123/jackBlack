from deck import Deck
from player import Player
from player import Dealer
from player import Hand
from card import Card

class BlackJack:
    def __init__(self):
        player1 = Player("")
        dealer = Dealer("mr.dealer")
        deck = Deck()


    def run(self):
        setup()

        bet()
        deal()
        playerAction()
        dealerAction()
        endGame()

    def drawBoard(self):
        Print("")
        # draww all cards 
        #2 draws for flip

    def setup(self):
        Print(f"{self.dealer.name}: Hello welcome to blackJack!\nWhat is your name?")
        self.player1.name = input().title()
        self.deck.shuffle()

    def bet(self):
        Print("")

card1 = Card('dimonds','2')
card1.reveal()
card1.position = 'set'
for line in card1.card2string():
    print(line)

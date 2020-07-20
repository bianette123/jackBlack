
class Player :

    def __init__(self, name):
        self.name = name
        self.money = 50
        self.hand = Hand()

    def bet(self):
        print(f"You have {self.money}\nHow much do you want to bet?\n")
        while True:
            try:
                bet = int(input())
            except ValueError:
                print('pick a number stupid!')   
            else:
                if bet > self.money :
                    print("you are too poor!")
                else:
                    break
        return bet

    def action(self):
        print('Hit or Stay')
        while True:
            action = input().lower()
            if action == 'hit':
                return action 
            elif action == 'stay':
                return action
            else:
                print('not vaid')

#dealer is child of parent player                 
class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)

    def deal(self, player, deck,cNum = 2):
        draw =[] 
        for i in range(cNum):
            topCard = deck.cards.pop()
            draw.append(topCard)
        for card in draw :
            player.hand.cards.append(card)
        

    def action(self):
        if self.hand.value() < 17:
            return ('hit')
        else:
            return ('stay')

    def bet(self):
        print('dealers dont bet dummy')

class Hand:
    def __init__(self):
        self.cards = []
        self.cardNum = len(self.cards)
        self.value = 0
        

    def updateValue(self, ace_value = 'low'):
        #create a dictionary for values
        values={
                'A': 1 ,
                '2': 2 ,
                '3': 3 ,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'J': 10,
                'Q': 10,
                'K': 10,
                }
        value = 0
        for card in self.cards:
            if card.rank == 'A' and ace_value.lower() == 'high':
                value += 10
            else:
                value += values[card.rank]
        
        self.value = value  

    def checkAce(self):
        for card in self.cards:
            if card.rank == 'A':
                return True
            else:
                return False

    def display(self):
        for card in self.cards :
            card.reveal()


                   
                    
                


        








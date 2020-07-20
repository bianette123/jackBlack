class Card :
    ''' class that represents a playing card '''

    #init runs @ beginnig 2 make basic info that object needs when its created 
    #self refers to card class(itself) 
    def __init__(self, suit, rank):  
        #self refers to the name that will be given to the instance of obj 
        self.suit = suit
        self.rank = rank
        self.position = 'down'
        self.value = 0

    def reveal(self):
        print(f"you have a {self.rank} of {self.suit}")
        self.position = 'up'



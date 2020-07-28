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

    def card2string(card = 0):
        suits_symbols = ['♠', '♦', '♥', '♣']
        if card.rank == '10':  
            space = '' 
        else: 
            space = '   ' 

        if card.suit == 'spades':
            suitSYB = suits_symbols[0]
        elif card.suit == 'cloves':
            suitSYB = suits_symbols[3]
        elif card.suit == 'hearts':
            suitSYB = suits_symbols[2]
        else:
            suitSYB = suits_symbols[1]


        if card==0: 
            fd00="   .............   "
            fd01="  :             :  "           
            fd02="  :             :  "
            fd03="  :             :  "
            fd04="  :             :  "
            fd05="  :             :  "
            fd06="  :             :  "
            fd07="  :             :  "
            fd08="  :             :  "
            fd09="  :             :  "
            fd10="  :.............:  "
            fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
            return fd
        else:
            if card.position.lower()=="set":
                 fd00="  ________________ " 
                 fd01=" |                |" 
                 fd02=" |{}{}            |".format(card.rank,space)
                 fd03=" |                |"
                 fd04=" |                |"
                 fd05=" |      {}         |".format(suitSYB)
                 fd06=" |                |"
                 fd07=" |                |"
                 fd08=" |                |"
                 fd09=" |           {}{} |".format(space,card.rank)
                 fd10=" |________________|" 
                 fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
                 return fd
            elif card.position.lower()=="face down":
                 fd00="  ________________ " 
                 fd01=" |      ____      |"  
                 fd02=" |     /    \     |"
                 fd03=" |    |      |    |"
                 fd04=" |    |      |    |"
                 fd05=" |    |      |    |"
                 fd06=" |    |      |    |"
                 fd07=" |    |      |    |"
                 fd08=" |    |      |    |"
                 fd09=" |     \____/     |"
                 fd10=" |________________|" 
                 fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
                 return fd





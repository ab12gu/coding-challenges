## filename: code-challenge -- ouster
# by: abhay gupta
#
# desc: play a game in a dec of cards
##         card class, player class

class Player(object):
    def age(self):
        print("many")

class Card(object):
    def __init__(self):
        self.amount = 52
        self.suites = ["spades", "diamond", "clover", "hearts"]
        self.numbers = 10
        self.faces = 4
        self.faces_values = ["jack", "queen", "king", "ace"]
        print('ARE YOU RUNNING')
        
        #self.deck = []
        
    def pick_card(self):
        print("temp")
    
    def create_deck(self, deck):
        
        for i in self.suites:
            for j in range(0, self.numbers):
                deck.append([i,j]) 
              
            for n in range(0, self.faces):
                deck.append([i,n])
                
        self.deck = deck
        
    def mix(self):  
        print("nobody")
        

if __name__ == "__main__":
    #Card() ## call class
    #print(Card().suites)
    deck = Card()
    deck.create_deck([])
    print(deck.deck[0])
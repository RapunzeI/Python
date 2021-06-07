import random
class Deck:
    def __init__(self, lst):
        self.lst = lst
    
    def shuffle(self):
        random.shuffle(self.lst)
    
    def dealCard(self):
        return self.lst.pop()

deck = Deck(['1', '2', '3', '4'])
deck.shuffle()
print(deck.dealCard())
print(deck.dealCard())

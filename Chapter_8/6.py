class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def __repr__(self):
        return "Card('{}', '{}')".format(self.rank, self.suit)
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

print(Card('3', 'Spade') == Card('3', 'Spade'))
print(Card('3', 'spade') == eval(repr(Card('3', 'spade'))))
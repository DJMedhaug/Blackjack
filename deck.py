from card import Card
from random import shuffle

class Deck(object):
    def __init__(self):
        suits = [" of Hearts", " of Spades", " of Diamonds", " of Clubs"]
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)
 
    def deal_card(self):
        return self.cards.pop()
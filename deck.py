from card import Card
from random import shuffle


class Deck(object):
    def __init__(self):
        suits = (" Hearts", " Spades", " Diamonds", " Clubs")
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T",
                 "J", "Q", "K")
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self): return self.cards.pop()

    
#         self.test_hand1 = {0: 'Ace of Spades', 1: 'Jack of Clubs' } # for testing
#         self.test_hand2 = {0: 'Ace of Clubs', 1: '10 of Diamonds' } # for testing
#         self.test_hand3 = {0: '8 of Spades', 1: '8 of Hearts'} # for testing splits
# ​
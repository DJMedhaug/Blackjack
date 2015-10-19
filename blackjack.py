__author__ = 'danamedhaug'

import random


class Card():
    """Base class for all cards"""

    suit = ["Hearts", "Spades", "Diamonds", "Clubs"]
    cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, value=value, suit=suit, cards=cards):
        self.value = value
        self.suit = suit
        self.cards = cards


# def deckGenerator(self):
#         # Creates a new deck of 52 cards in a standard order
#
#
#  def shuffle(self):
#         # shuffle the Card
#          # use random.shuffle()
#
#  def draw_card(self):
#         # Draw card from deck
#
#
#  def cards_left  (self):
#         # Cards left in the deck
#
#
#  def sort(self):
#         # Sorts the cards back into standard order
#
#
#
#

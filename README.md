# Blackjack
blackjack project
A simple program to play Blackjack on the terminal. Run main.py to play.

```
class Deck(object):
    """ deck class that shuffles and distributes cards.
    """
    def __init__(self):
        suits = (" Hearts", " Spades", " Diamonds", " Clubs")
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T",
                 "J", "Q", "K")
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self): return self.cards.pop()
```

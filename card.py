class Card(object):
    """Returns value of a card in a hand.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

    def card_value(self):
        if self.rank in "TJQK":
            # In 10 of the top ten,J,Q,K.
            return 10
        else:
            # Returns the number of points required for any other card.
            # Ace initially gives 1 point.
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

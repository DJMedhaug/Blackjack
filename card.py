class Card(object):
    """Returns value of a card in players hand.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

    def card_value(self):
        if self.rank in "TJQK":  # Ten, Jack, Queen, King = 10 points.
            return 10
        else:
            # assert self.rank == "J"
            return " A23456789".index(self.rank)  # Ace initially gives 1 point.

    def get_rank(self):
        return self.rank

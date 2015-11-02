from card import Card
from deck import Deck
from hand import Hand
from colorama import Fore, Back, Style
from colorama import init
init()


def reset_game():
    """Function called to start Blckjack
    """
    d = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("*" * 25)
    print(player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        ans = input("Press h to Hit or any to stand? ")
        if ans.lower() == "h":
            player_hand.add_card(d.deal_card())
            print("You Hit!")
            print(player_hand)
            if player_hand.get_value() > 21:
                print(Fore.RED + "YOU LOSE!!")
                in_game = False
        else:
            print("You Stand!")
            break
    print("*" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print(Fore.GREEN + " DEALER BUSTS...YOU WIN!!")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print(Fore.GREEN + " YOU WIN!!")
        else:
            print(Fore.RED + " DEALER WINS!!")

reset_game()

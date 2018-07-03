# A class used to create the 52 card deck
# Suites are clubs, diamonds, hearts and spades
# Ranks are 1-10, jack, queen and king

import enum
from random import shuffle


class Suites(enum.Enum):
    __ordering__ = "CLUBS DIAMONDS HEARTS SPADES"
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'
    HEARTS = 'hearts'
    SPADES = 'spades'


class Ranks(enum.Enum):
    __ordering__ = "ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING"
    ACE = 'ace'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'
    TEN = 'ten'
    JACK = 'jack'
    QUEEN = 'queen'
    KING = 'king'


class Deck:
    deck = []
    drawn_cards = []
    dealer_hand = []
    player_one_hand = []
    card_count = 0

    def __init__(self):
        # deck = []
        cards = {}
        value = 1
        for suite in Suites:
            for rank in Ranks:
                key_name = ("%s of %s" % (rank.value, suite.value))
                cards[key_name] = value
                if rank.value in ['ten', 'jack', 'queen']:
                    continue
                elif rank.value == 'king':
                    value = 1
                else:
                    value += 1
        for key, value in cards.items():
            temp = [key, value]
            self.deck.append(temp)

    def show_deck(self):
        print(self.deck)
        print(len(self.deck), "cards in deck")

    def shuffle_deck(self):
        for _ in range(3):
            shuffle(self.deck)

    # Draw method which is used to remove two cards for each player
    # Number of players is so we can get the correct number of cards for all of players
    # Draw one card for each player, per iteration, until each player has received a card
    # This goes counter clockwise, starting with the dealer, and then proceeds from there
    def create_starting_hands(self):
        self.draw_card(player=True, dealer=True)
        self.draw_card(player=True, dealer=True)

    def show_hand(self, player=False, dealer=False):
        if player == True and dealer == True:
            print("Dealer: %s " % self.dealer_hand)
            print("Player one: %s" % self.player_one_hand)
        elif player == True and dealer == False:
            print("Player one: %s" % self.player_one_hand)
        elif player == False and dealer == True:
            print("Dealer: %s " % self.dealer_hand)

    def draw_card(self, player=False, dealer=False):
        if player == True and dealer == True:
            dealer_card = self.deck.pop()
            player_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            self.player_one_hand.append(player_card)
            self.card_count += 2
            return dealer_card, player_card
        elif player == True and dealer == False:
            player_card = self.deck.pop()
            self.player_one_hand.append(player_card)
            self.card_count += 1
            return player_card
        elif player == False and dealer == True:
            dealer_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            self.card_count += 1
            return dealer_card

    def get_card_count(self):
        print("The card count is currently: %d" % self.card_count)
        if self.card_count < 48:
            print("Draw card")
        else:
            print("Deck needs to be recreated and shuffled.")

def make_deck():
    deck = Deck()
    return deck

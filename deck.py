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
    dealer_hand_is_soft = False
    player_one_hand = []
    player_one_hand_is_soft = False
    graveyard = []
    card_count = 0

    def __init__(self):
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

    # A function used to shuffle the deck three times
    def shuffle_deck(self):
        for _ in range(3):
            shuffle(self.deck)

    # A function which is used to remove two cards for each player
    # We draw one card for each player, per iteration, until both the player and dealer have received a card
    # This goes counter clockwise, starting with the dealer, and then proceeds from there
    def create_starting_hands(self):
        self.draw_card(player=True, dealer=True)
        self.draw_card(player=True, dealer=True)

    def show_hand(self, player=False, dealer=False):
        if player is True and dealer is True:
            print("\nDealer: %s " % self.dealer_hand)
            print("Player one: %s" % self.player_one_hand)
        elif player is True and dealer is False:
            print("\nDealer: %s " % self.dealer_hand[0])
            print("Player one: %s" % self.player_one_hand)
        elif player is False and dealer is True:
            print("\nDealer: %s " % self.dealer_hand)

    def draw_card(self, player=False, dealer=False):
        if player is True and dealer is True:
            dealer_card = self.deck.pop()
            player_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            self.player_one_hand.append(player_card)
            return dealer_card, player_card
        elif player is True and dealer is False:
            player_card = self.deck.pop()
            self.player_one_hand.append(player_card)
            return player_card
        elif player is False and dealer is True:
            dealer_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            return dealer_card

    def reset_hands(self, print_graveyard=False):
        play_hand = True
        deal_hand = True
        while play_hand:
            if not self.player_one_hand:
                play_hand = False
            else:
                self.graveyard.append(self.player_one_hand.pop())
        while deal_hand:
            if not self.dealer_hand:
                deal_hand = False
            else:
                self.graveyard.append(self.dealer_hand.pop())
        if print_graveyard is True:
            for card in self.graveyard:
                print(f"{card[0]}")

    # A function used to check how many cards have been drawn out of the main deck
    # If the number of cards is greater than or equal to 46 then we empty the graveyard back into the deck and shuffle it
    def check_graveyard(self):
        _graveyard_count = 0
        _graveyard = True
        for _ in self.graveyard:
            _graveyard_count += 1
        print(f"Graveyard count = {_graveyard_count}")
        if _graveyard_count >= 46:
            print("Time to create a new deck. AKA Shuffle the deck and reset the graveyard.")
            while _graveyard:
                if not self.graveyard:
                    _graveyard = False
                else:
                    self.deck.append(self.graveyard.pop())
        self.shuffle_deck()

def make_deck():
    deck = Deck()
    return deck

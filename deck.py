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

class Deck():
    deck = []
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
            if value == 1:
                temp = [key, [value, 11]]
                self.deck.append(temp)
            else:
                temp = [key, value]
                self.deck.append(temp)

    def show_deck(self):
        print(self.deck)
        print(len(self.deck), "cards in deck")

    def shuffle_deck(self):
        for x in range(3):
            shuffle(self.deck)

def make_deck():
    deck = Deck()
    return deck
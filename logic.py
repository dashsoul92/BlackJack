# A class used to control the logic of the game


class Logic:
    __p1_score__ = 0
    __dealer_score__ = 0
    deck = []

    def __init__(self, deck):
        self.__p1_score__ = 0
        self.__dealer_score__ = 0
        self.deck = deck

    # Method used to get all of the players scores
    def get_score(self, player=False, dealer=False):
        busted = False
        if (player == True) and (dealer == True):
            self.__p1_score__ = 0
            for card in self.deck.player_one_hand:
                self.__p1_score__ += int(card[1])
            print("\nThe player's score is: " + str(self.__p1_score__))

            self.__dealer_score__ = 0
            for card in self.deck.dealer_hand:
                self.__dealer_score__ += int(card[1])
            return busted
        elif (player == True) and (dealer == False):
            self.__p1_score__ = 0
            for card in self.deck.player_one_hand:
                if self.__p1_score__ + int(card[1]) > 21:
                    self.__p1_score__ += int(card[1])
                    print("\nYour score was: " + str(self.__p1_score__))
                    busted = True
                    return busted
                else:
                    self.__p1_score__ += int(card[1])
            print("\nYour score is: " + str(self.__p1_score__))
            return busted
        elif (player == False) and (dealer == True):
            for card in self.deck.dealer_hand:
                if self.__dealer_score__ + int(card[1]) > 21:
                    self.__dealer_score__ + int(card[1])
                    print("\nThe Dealer's score is: " + str(self.__p1_score__))
                    busted = True
                    return busted
                else:
                    self.__dealer_score__ += int(card[1])
                    print("\nThe Dealer's score is: " + str(self.__p1_score__))
            return busted

# A method used to create logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

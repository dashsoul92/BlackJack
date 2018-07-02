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
            for card in self.deck.player_one_hand:
                if self.__p1_score__ + int(card[1]) > 21:
                    print("Player one busted!")
                    self.__p1_score__ += int(card[1])
                    busted = True
                    return busted
                else:
                    self.__p1_score__ += int(card[1])
                # print(card)
            print("\nThe player's score is: " + str(self.__p1_score__))

            for card in self.deck.dealer_hand:
                if self.__dealer_score__ + int(card[1]) > 21:
                    print("The dealer busted!")
                    self.__dealer_score__ += int(card[1])
                else:
                    self.__dealer_score__ += int(card[1])
                # print(card)
            print("The dealer's score is: " + str(self.__dealer_score__))
            return self.__p1_score__, self.__dealer_score__
        elif (player == True) and (dealer == False):
            for card in self.deck.player_one_hand:
                if self.__p1_score__ + int(card[1]) > 21:
                    print("Player one busted!")
                    self.__p1_score__ += int(card[1])
                    busted = True
                    return busted
                else:
                    self.__p1_score__ += int(card[1])
                # print(card)
            print("\nThe player's score is: " + str(self.__p1_score__))
        elif (player == False) and (dealer == True):
            for card in self.deck.dealer_hand:
                if self.__dealer_score__ + int(card[1]) > 21:
                    print("The dealer busted!")
                    self.__dealer_score__ += int(card[1])
                else:
                    self.__dealer_score__ += int(card[1])
                # print(card)
            print("The dealer's score is: " + str(self.__dealer_score__))
            return self.__dealer_score__

# A method used to create logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

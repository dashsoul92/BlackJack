# A class used to control the logic of the game


class Logic:
    __p1_score__ = 0
    __dealer_score__ = 0
    deck = []

    def __init__(self, deck):
        self.__p1_score__ = 0
        self.__dealer_score__ = 0
        self.deck = deck

    # Method used to set the scores
    def set_score(self):
        self.__dealer_score__ = 0
        self.__p1_score__ = 0
        for card in self.deck.dealer_hand:
            self.__dealer_score__ += card[1]
        for card in self.deck.player_one_hand:
            self.__p1_score__ += card[1]
        return self.__dealer_score__, self.__p1_score__

    # Method used to evaluate the scores
    def check_score(self, dealer=False, player=False, print_score=False):
        self.set_score()
        if dealer == True and player == True and print_score == True:
            print(f"\nThe dealer's score is: {self.__dealer_score__}")
            print(f"The player's score is {self.__p1_score__}")
            return self.__dealer_score__, self.__p1_score__
        elif dealer == True and player == True and print_score == False:
            return self.__dealer_score__, self.__p1_score__
        elif dealer == True and player == False:
            return self.__dealer_score__
        elif dealer == False and player == True:
            return self.__p1_score__
        else:
            return


# A method used to create the logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

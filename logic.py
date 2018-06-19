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
    def get_scores(self):
        for card in self.deck.player_one_hand:
            self.__p1_score__ += int(card[1])
            # print(card)
        print("\nThe player's score is: " + str(self.__p1_score__))
        for card in self.deck.dealer_hand:
            self.__dealer_score__ += int(card[1])
            # print(card)
        print("The dealer's score is: " + str(self.__dealer_score__))
        return self.__p1_score__, self.__dealer_score__

# A method used to create logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

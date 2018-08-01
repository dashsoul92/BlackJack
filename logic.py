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
        self.deck.dealer_hand_is_soft = False
        self.deck.player_one_hand_is_soft = False
        for card in self.deck.dealer_hand:              
             if self.deck.dealer_hand_is_soft == False:     # MAIN Case where no aces in hand OR ace is vaule of 1
               if card[1] == 1:
                  if self.__dealer_score__ + 11 > 21:         # Case where ace is value of 1
                     self.__dealer_score__ += card[1]
                  else:
                       self.__dealer_score__ += 11            # Case where ace is value of 11
                       self.deck.dealer_hand_is_soft = True
               else:                                          # Case for all other cards
                   self.__dealer_score__ += card[1]        
             else:                                          # MAIN Case where ace is in hand and is value of 11
                 if card[1] == 1:                             # Case where additional ace is drawn
                   if self.__dealer_score__ + 1 > 21:           # Both ace values are 1
                      self.__dealer_score__ += card[1]
                      self.__dealer_score__ -= 10
                      self.deck.dealer_hand_is_soft = False
                   else:                                        # Ace in hand remains value of 11 and drawn ace is value of 1
                        self.__dealer_score__ += card[1]
                        self.deck.dealer_hand_is_soft = True
                 else:                                        # Case where any other card is drawn
                      if self.__dealer_score__ + card[1] > 21:  # Ace in hand reduced to value of 1
                         self.__dealer_score__ += card[1]
                         self.__dealer_score__ -= 10
                         self.deck.dealer_hand_is_soft = False
                      else:                                     # Ace remains value of 11
                            self.__dealer_score__ += card[1]
                            self.deck.dealer_hand_is_soft = True
        for card in self.deck.player_one_hand:
            if self.deck.player_one_hand_is_soft == False:
               if card[1] == 1:
                  if self.__p1_score__ + 11 > 21:
                     self.__p1_score__ += card[1]
                  else:
                       self.__p1_score__ += 11
                       self.deck.player_one_hand_is_soft = True
               else:
                   self.__p1_score__ += card[1]
            else:
                 if card[1] == 1:
                   if self.__p1_score__ + 1 > 21:
                      self.__p1_score__ += card[1]
                      self.__p1_score__ -= 10
                      self.deck.player_one_hand_is_soft = False
                   else:
                        self.__p1_score__ += card[1]
                        self.deck.player_one_hand_is_soft = True
                 else:
                      if self.__p1_score__ + card[1] > 21:
                         self.__p1_score__ += card[1]
                         self.__p1_score__ -= 10
                         self.deck.player_one_hand_is_soft = False
                      else:
                            self.__p1_score__ += card[1]
                            self.deck.player_one_hand_is_soft = True
            
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
        elif dealer == False and player == False and print_score == True:
            print(f"\nThe dealer's score is: {self.__dealer_score__}")
            print(f"The player's score is {self.__p1_score__}")
        else:
            return

    # Method used to handle logic for each round of the game
    def play_round(self, deck, logic, game_number=0):
        game_round = True
        state = 0

        while game_round:
            # Game setup
            if state is 0:
                # The beginning of a round
                # Create dealer and player hands
                deck.create_starting_hands()
                deck.show_hand(dealer=True, player=True)
                state = 1
            # Game controller for hitting and standing as the player
            elif state is 1:
                player_score = logic.check_score(player=True)
                if player_score == 21:
                    state = 2
                elif player_score < 21:
                    logic.check_score(dealer=True, player=True, print_score=True)
                    while True:
                           try:
                               player_response = str(input("Type 'h' to hit or 's' to stand: "))
                               if player_response not in (['h','s', 'dd','i','gg']):
                                  raise ValueError
                               break
                           except ValueError:
                                  print(player_response + " is an invalid input.")
                    # Hitting
                    if player_response == 'h':
                        deck.draw_card(player=True)
                    # Standing
                    elif player_response == 's':
                        state = 2
                elif player_score > 21:
                    dealer_score, player_score = logic.check_score(dealer=True, player=True, print_score=False)
                    print(f"\nThe dealer won with a score of: {dealer_score}."
                          f"\nThe player busted with a score of: {player_score}.")
                    game_number += 1
                    deck.show_hand(dealer=True, player=True)
                    deck.reset_hands()
                    deck.check_graveyard()
                    game_round = False
                    return game_number
            # Dealer logic for hitting and standing
            # If the dealer's hand is 17 or higher then, the dealer will always stand
            # If the dealer's hand is less than 17 then, the dealer must hit
            elif state is 2:
                dealer_score, player_score = logic.check_score(dealer=True, player=True)
                if dealer_score >= 17 and dealer_score <= 21:
                    if dealer_score > player_score:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                              f"\nThe player lost with a score of: {player_score}.")
                        game_number += 1
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                    elif dealer_score < player_score:
                        print(f"\nThe dealer lost with a score of: {dealer_score}."
                              f"\nThe player won with a score of: {player_score}.")
                        game_number += 1
                        deck.show_hand()
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                    else:
                        print(f"\nIt was a push. Both the player and dealer had a score of: {dealer_score}.")
                        game_number += 1
                        deck.show_hand()
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                elif dealer_score < 17:
                    deck.draw_card(dealer=True)
                    dealer_score = logic.check_score(dealer=True)
                    if dealer_score == 21:
                        player_score = logic.check_score(player=True)
                        if player_score == 21:
                            print(f"It was a push. Both the player and dealer had a score of: {dealer_score}")
                            game_number += 1
                            deck.show_hand(dealer=True, player=True)
                            deck.reset_hands()
                            deck.check_graveyard()
                            game_round = False
                            return game_number
                        else:
                            print(f"\nThe dealer won with a score of: {dealer_score}. "
                                  f"\nThe player lost with a score of: {player_score}.")
                            game_number += 1
                            deck.show_hand(dealer=True, player=True)
                            deck.reset_hands()
                            deck.check_graveyard()
                            game_round = False
                            return game_number
                elif dealer_score > 21:
                    print(f"\nThe dealer busted with a score of: {dealer_score}."
                          f"\nThe player won with a score of: {player_score}")
                    game_number += 1
                    deck.show_hand(dealer=True, player=True)
                    deck.reset_hands()
                    deck.check_graveyard()
                    game_round = False
                    return game_number


# A method used to create the logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

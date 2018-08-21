# A class used to control the logic of the game


class Logic:
    __p1_score__ = 0
    __p1_score_2__ = 0
    __splits_done__ = 0
    __splits_allowed__ = 1
    __dealer_score__ = 0
    __player_score_list__ = []
    deck = []

    def __init__(self, deck):
        self.__p1_score__ = 0
        self.__p1_score_2__ = 0
        self.__splits_done__ = 0
        self.__splits_allowed__ = 1
        self.__dealer_score__ = 0
        self.__player_score_list__ = []
        self.deck = deck

    # Method used to set the scores
    def set_score(self, __has_split__ = False):
        self.__dealer_score__ = 0
        self.__p1_score__ = 0
        self.__p1_score_2__ = 0
        self.__player_score_list__ = []
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
        for player_one_hand in self.deck.player_one:
            self.__p1_score__ = 0
            for card in player_one_hand:
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
            __score_to_add_to_list__ = str(self.__p1_score__)
            self.__player_score_list__.append(__score_to_add_to_list__)
            
        if __has_split__ == True:
            return self.__dealer_score__, self.__player_score_list__
        else:
            return self.__dealer_score__, self.__p1_score__

    # Method used to evaluate the scores
    def check_score(self, dealer=False, player=False, print_score=False):       #look at this later
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
                # Handle Insurance bet
                __card_1__ = deck.dealer_hand[0]
                if __card_1__[1] == 10 or __card_1__[1] == 1:
                    deck.show_hand(dealer=False, player=True)
                    while True:
                           try:
                               player_response = str(input("Type 'y' to Surrender or 'n' to continue: "))
                               if player_response not in (['n','y']):
                                  raise ValueError
                               break
                           except ValueError:
                                  print(player_response + " is an invalid input.")
                           # Surrender
                    if player_response == 'y':
                        # add bet
                        print(f"\nYou Surrendered")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                    # Never Surrender!!!
                    elif player_response == 'n':
                        pass

                    while True:
                           try:
                               player_response = str(input("Type 'y' to make Insurance bet or 'n' to continue: "))
                               if player_response not in (['n','y']):
                                  raise ValueError
                               break
                           except ValueError:
                                  print(player_response + " is an invalid input.")
                    # Insurance bet
                    if player_response == 'y':
                       pass # add bet
                    # No bet
                    elif player_response == 'n':
                        pass
                    __dealer_score__ = logic.check_score(dealer=True)
                    if __dealer_score__ == 21:
                        # pay insurance
                        state = 2 # assume all bets can be handled in 2
                        continue
                    else:
                        # lose insurance
                        pass
                else:
                     deck.show_hand(dealer=False, player=True)
                     while True:
                           try:
                               player_response = str(input("Type 'y' to Surrender or 'n' to continue: "))
                               if player_response not in (['n','y']):
                                  raise ValueError
                               break
                           except ValueError:
                                  print(player_response + " is an invalid input.")
                     # Surrender
                     if player_response == 'y':
                        # add bet
                        print(f"\nYou Surrendered.")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                     # Never Surrender!!!
                     elif player_response == 'n':
                         pass

                deck.show_hand(dealer=True, player=True)
                state = 1
            # Game controller for hitting and standing as the player
            elif state is 1:
                player_score = logic.check_score(player=True)
                if player_score == 21:
                    state = 2
                elif player_score < 21:
                    logic.check_score(dealer=True, player=True, print_score=True)
                    player_one_hand = deck.player_one[0]
                    card_1 = player_one_hand[0]
                    card_2 = player_one_hand[1]
                    if card_1[1] == card_2[1] and self.__splits_done__ < self.__splits_allowed__:
                        while True:
                           try:
                               player_response = str(input("Type 'y' to split or 'n' to continue: "))
                               if player_response not in (['n','y']):
                                  raise ValueError
                               break
                           except ValueError:
                                  print(player_response + " is an invalid input.")
                        # Splitting
                        if player_response == 'y':
                            deck.split_hand()
                            deck.draw_card(player=True)
                            state = 3
                            continue
                        # Not Splittng
                        elif player_response == 'n':
                            pass
                    while True:
                           try:
                               player_response = str(input("Type 'h' to hit or 's' to stand: "))
                               if player_response not in (['h','s', 'dd']):
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
                if dealer_score >= 17 and dealer_score <= 21 or player_score == 21:
                    if dealer_score > player_score:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                              f"\nThe player lost with a score of: {player_score}.")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                    elif dealer_score < player_score:
                        print(f"\nThe dealer lost with a score of: {dealer_score}."
                              f"\nThe player won with a score of: {player_score}.")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                    else:
                        print(f"\nIt was a push. Both the player and dealer had a score of: {dealer_score}.")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
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
                            __splits_done__ = 0
                            deck.show_hand(dealer=True, player=True)
                            deck.reset_hands()
                            deck.check_graveyard()
                            game_round = False
                            return game_number
                        else:
                            print(f"\nThe dealer won with a score of: {dealer_score}. "
                                  f"\nThe player lost with a score of: {player_score}.")
                            game_number += 1
                            __splits_done__ = 0
                            deck.show_hand(dealer=True, player=True)
                            deck.reset_hands()
                            deck.check_graveyard()
                            game_round = False
                            return game_number
                elif dealer_score > 21:
                    print(f"\nThe dealer busted with a score of: {dealer_score}."
                          f"\nThe player won with a score of: {player_score}")
                    game_number += 1
                    __splits_done__ = 0
                    deck.show_hand(dealer=True, player=True)
                    deck.reset_hands()
                    deck.check_graveyard()
                    game_round = False
                    return game_number
            #same as state 1 but for split hands
            elif state is 3:
                __has_split__ = True
                __p1_hand_actions_done__ = False
                __p1_hand_2_actions_done__ = False
                while True:
                    self.set_score(__has_split__)
                    __p1_score__ = int(self.__player_score_list__[0])
                    __p1_score_2__ = int(self.__player_score_list__[1])
                    player_score = __p1_score__
                    deck.show_hand(player=True, dealer=True)
                    if player_score >= 21:
                        __p1_hand_actions_done__ = True
                    player_score = __p1_score_2__
                    if player_score >= 21:
                        __p1_hand_2_actions_done__ = True

                    if __p1_hand_actions_done__ == True and __p1_hand_2_actions_done__ == True:
                        state = 4
                        break
                    elif __p1_hand_actions_done__ == True and __p1_hand_2_actions_done__ == False:
                        print(f"\nThe dealer's score is: {self.__dealer_score__}")
                        print(f"The player's scores are: {__p1_score__}, {__p1_score_2__}")
                        while True:
                               try:
                                   player_response = str(input("Type 'h' to hit or 's' to stand for hand 2: "))
                                   if player_response not in (['h','s', 'dd']):
                                      raise ValueError
                                   break
                               except ValueError:
                                      print(player_response + " is an invalid input.")
                        # Hitting
                        if player_response == 'h':
                           # playing_hand = deck.player_one[1]
                            deck.draw_single_card(hand_1=False)
                        # Standing
                        elif player_response == 's':
                            __p1_hand_2_actions_done__ = True
                               
                    elif __p1_hand_actions_done__ == False and __p1_hand_2_actions_done__ == True:
                        print(f"\nThe dealer's score is: {self.__dealer_score__}")
                        print(f"The player's scores are: {__p1_score__}, {__p1_score_2__}")
                        while True:
                               try:
                                   player_response = str(input("Type 'h' to hit or 's' to stand for hand 1: "))
                                   if player_response not in (['h','s', 'dd']):
                                      raise ValueError
                                   break
                               except ValueError:
                                      print(player_response + " is an invalid input.")
                        # Hitting
                        if player_response == 'h':
                            deck.draw_single_card(hand_1=True)
                        # Standing
                        elif player_response == 's':
                            __p1_hand_actions_done__ = True
                                
                    else:
                        print(f"\nThe dealer's score is: {self.__dealer_score__}")
                        print(f"The player's scores are: {__p1_score__}, {__p1_score_2__}")
                        while True:
                               try:
                                   player_response = str(input("Type 'h' to hit or 's' to stand for hand 1: "))
                                   if player_response not in (['h','s', 'dd']):
                                      raise ValueError
                                   break
                               except ValueError:
                                      print(player_response + " is an invalid input.")
                        # Hitting
                        if player_response == 'h':
                            deck.draw_single_card(hand_1=True)
                        # Standing
                        elif player_response == 's':
                            __p1_hand_actions_done__ = True

                        while True:
                               try:
                                   player_response = str(input("Type 'h' to hit or 's' to stand for hand 2: "))
                                   if player_response not in (['h','s', 'dd']):
                                      raise ValueError
                                   break
                               except ValueError:
                                      print(player_response + " is an invalid input.")
                        # Hitting
                        if player_response == 'h':
                            deck.draw_single_card(hand_1=False)
                        # Standing
                        elif player_response == 's':
                            __p1_hand_2_actions_done__ = True
            # same as state 1 bt for split hands                
            elif state is 4:
                dealer_score = logic.check_score(dealer=True)
                player_score_1 = __p1_score__
                player_score_2 = __p1_score_2__
                one_hand_busted = False
                if player_score_1 > 21 or player_score_2 > 21:
                    if player_score_1 > 21 and player_score_2 > 21:
                            print(f"\nThe dealer won with a score of: {dealer_score}."
                            f"\nThe player busted with scores of: {player_score_1}, {player_score_2}.")
                            continue
                    elif player_score_1 > 21 and player_score_2 <= 21:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                            f"\nThe player 1 hand busted with score of: {player_score_1}.")
                        one_hand_busted = True
                        player_score_1 = dealer_score
                    elif player_score_2 > 21 and player_score_1 <= 21:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                            f"\nThe player 2 hand busted with score of: {player_score_2}.")
                        one_hand_busted = True
                        player_score_2 = dealer_score
                           
                if dealer_score >= 17 and dealer_score <= 21:
                    if dealer_score > player_score_1:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                              f"\nThe player hand 1 lost with a score of: {player_score_1}.")
                    elif dealer_score < player_score_1:
                        print(f"\nThe dealer lost with a score of: {dealer_score}."
                              f"\nThe player hand 1 won with a score of: {player_score_1}.")
                    elif one_hand_busted == True:
                        pass
                    else:
                        print(f"\nIt was a push. Both the player hand 1 and dealer had a score of: {dealer_score}.")

                    if dealer_score > player_score_2:
                        print(f"\nThe dealer won with a score of: {dealer_score}."
                              f"\nThe player hand 2 lost with a score of: {player_score_2}.")
                    elif dealer_score < player_score_2:
                        print(f"\nThe dealer lost with a score of: {dealer_score}."
                              f"\nThe player hand 2 won with a score of: {player_score_2}.")
                    elif one_hand_busted == True:
                        pass
                    else:
                        print(f"\nIt was a push. Both the player hand 2 and dealer had a score of: {dealer_score}.")

                    game_number += 1
                    __splits_done__ = 0
                    deck.show_hand(dealer=True, player=True)
                    deck.reset_hands()
                    deck.check_graveyard()
                    game_round = False
                    return game_number
                elif dealer_score < 17:
                    deck.draw_card(dealer=True)
                    dealer_score = logic.check_score(dealer=True)
                    if dealer_score == 21:
                        if player_score_1 == 21:
                            print(f"It was a push. Both the player hand 1 and dealer had a score of: {dealer_score}")
                        elif one_hand_busted == True:
                            pass
                        else:
                            print(f"\nThe dealer won with a score of: {dealer_score}. "
                                  f"\nThe player hand 1 lost with a score of: {player_score_1}.")
                        if player_score_2 == 21:
                            print(f"It was a push. Both the player hand 2 and dealer had a score of: {dealer_score}")
                        elif one_hand_busted == True:
                            pass
                        else:
                            print(f"\nThe dealer won with a score of: {dealer_score}. "
                                  f"\nThe player hand 2 lost with a score of: {player_score_2}.")
                        game_number += 1
                        __splits_done__ = 0
                        deck.show_hand(dealer=True, player=True)
                        deck.reset_hands()
                        deck.check_graveyard()
                        game_round = False
                        return game_number
                elif dealer_score > 21:
                    if one_hand_busted == False:
                        print(f"\nThe dealer busted with a score of: {dealer_score}."
                          f"\nThe player won with a scores of: {player_score_1, player_score_2}")
                    else:
                        if player_score_1 < dealer_score:
                            print(f"\nThe dealer busted with a score of: {dealer_score}."
                                f"\nThe player hand 1 with a score of: {player_score_1}")
                        else:
                            print(f"\nThe dealer busted with a score of: {dealer_score}."
                                 f"\nThe player hand 2 won with a score of: {player_score_2}")
                    game_number += 1
                    __splits_done__ = 0
                    deck.show_hand(dealer=True, player=True)
                    deck.reset_hands()
                    deck.check_graveyard()
                    game_round = False
                    return game_number


                


# A method used to create the logic object
def create_logic(deck):
    logic = Logic(deck)
    return logic

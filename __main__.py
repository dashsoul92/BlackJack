import deck
import logic


# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.shuffle_deck()

# Create logic object
game_logic = logic.create_logic(bj_deck)

state = 0
game = True
while game:
    if state == 0:
        # The beginning of a round
        # Create dealer and player one's hands
        bj_deck.create_starting_hands()
        state = 1
    elif state == 1:
        bj_deck.show_hand(player=True, dealer=True)
        busted, player_score = game_logic.get_score(player=True)
        player_response = input("Type 'h' to hit or 's' to stay: ")

        if player_response == 'h':
            print("hit")
            bj_deck.show_hand(player=True, dealer=True)
            bj_deck.draw_card(player=True)
            busted, player_score = game_logic.get_score(player=True)
            if busted == True:
                print("You busted! Dealer wins.")
                game = False
            else:
                continue
        elif player_response == 's':
            print("\nThe player is staying!")
            game_logic.get_score(player=True, dealer=False)
            state = 2
    elif state == 2:
        busted = False
        busted, dealer_score = game_logic.get_score(dealer=True)
        if dealer_score <= 16:
            print("Hit")
            bj_deck.draw_card(dealer=True)
            busted, dealer_score = game_logic.get_score(dealer=True)
            if busted == True:
                print("The Dealer's score was: %d" % dealer_score)
                print("The Dealer busted! You win.")
                game = False
        else:
            bj_deck.draw_card()
            player_busted, dealer_busted, player_score, dealer_score = game_logic.get_score(player=True, dealer=True)
            if player_busted == True:
                print("The dealer wins")
                game = False
            elif dealer_busted == True:
                print("The dealer wins!")
            elif player_busted != True and dealer_busted != True and player_score > dealer_score:
                print("The player won!")
                game = False
            elif player_busted != True and dealer_busted != True and player_score < dealer_score:
                print("The dealer won!")
                game = False
            elif player_busted != True and dealer_busted != True and player_score == dealer_score:
                print("It was a draw!")
                game = False
        continue
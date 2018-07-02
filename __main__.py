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
        game_logic.get_score(player=True, dealer=True)
        player_response = input("Type 'h' to hit or 's' to stay: ")

        if player_response == 'h':
            print("hit")
            bj_deck.draw_card(player=True)
            busted = game_logic.get_score(player=True)
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
        # TODO Work on dealer logic
        # if game_logic.get_score(dealer=True) <= 16:
        #     print("Hit")
        #     bj_deck.draw_card(dealer=True)
        #     busted = game_logic.get_score(dealer=True)
        #     if busted == True:
        #         print("The Dealer busted! You win.")
        #         game = False
        # else:
        #     continue
        continue
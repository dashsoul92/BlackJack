import deck
import logic

# TODO Create the logic for the dealer. Hitting and staying
# TODO Handle multiple rounds rather than just the one round
# TODO Handle placing bets
# TODO Handle keeping track of bank

# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.shuffle_deck()

# Create logic object
game_logic = logic.create_logic(bj_deck)

# Beginning the game
state = 0
game = True
while game:
    # Game setup
    if state == 0:
        # The beginning of a round
        # Create dealer and player hands
        bj_deck.create_starting_hands()
        state = 1
    # Game controller for hitting and standing as the player
    elif state == 1:
        dealer_score, player_score = game_logic.check_score(dealer=True, player=True, print_score=False)
        if player_score < 21:
            game_logic.check_score(dealer=True, player=True, print_score=True)
            player_response = input("Type 'h' to hit or 's' to stand: ")
            # Hitting
            if player_response == 'h':
                player_card = bj_deck.draw_card(player=True)
                if player_score > 21:
                    print(f"\nThe player busted with a score of: {player_score}. "
                          f"The dealer won with a score of: {dealer_score}")
                    game = False
                elif player_score < 21:
                    continue
                else:
                    print(f"\nThe player has blackjack!")
                    state = 2
            # Standing
            elif player_response == 's':
                state = 2
        else:
            game_logic.check_score(dealer=True, player=True, print_score=False)
            print(f"\nThe player busted with a score of: {player_score}."
                  f"\nThe dealer won with a score of: {dealer_score}.")
            game = False
    # Dealer logic for hitting and standing
    # If the dealer's hand is 17 or higher then, the dealer will always stand
    # If the dealer's hand is less than 17 then, the dealer must hit
    elif state == 2:
        dealer_score, player_score = game_logic.check_score(dealer=True, player=True)
        if dealer_score == 17:
            if dealer_score > player_score:
                print(f"\nThe dealer won with a score of: {dealer_score}."
                      f"\nThe player's score was: {player_score}.")
                game = False
            elif dealer_score < player_score:
                print(f"\nThe player won with a score of: {player_score}."
                      f"\nThe dealer's score was: {dealer_score}.")
                game = False
            else:
                print(f"\nIt was a push. Both the player and dealer had a score of: {dealer_score}.")
                game = False
        elif dealer_score < 17:
            dealer_card = bj_deck.draw_card(dealer=True)
            dealer_score = game_logic.check_score(dealer=True)
            if dealer_score == 21:
                player_score = game_logic.check_score(player=True)
                if player_score == 21:
                    print(f"It was a push. Both the player and dealer had a score of: {dealer_score}")
                    game = False
                else:
                    print(f"The dealer won with a score of: {dealer_score}. \nThe player's score was: {player_score}.")
                    game = False
        else:
            print(f"\nThe dealer busted with a score of: {dealer_score}."
                  f"The player won with a score of: {player_score}")
            game = False

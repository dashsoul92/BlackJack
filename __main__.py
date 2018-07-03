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
        # bj_deck.show_hand(player=True, dealer=True)
        game_logic.check_score(dealer=True, player=True)
        player_response = input("\nType 'h' to hit or 's' to stay: ")

        if player_response == 'h':
            print("Hit!")
            player_card = bj_deck.draw_card(player=True)
            player_score = game_logic.check_score(player=True)
            if player_score > 21:
                print(f"The player busted with a score of {player_score}")
                game = False
            elif player_score < 21:
                continue
            else:
                print(f"The player has blackjack!")
                game = False
        elif player_response == 's':
            print("\nThe player is staying!")
            state = 2
    elif state == 2:
        print("It's the dealer's turn!")
        game = False
        continue
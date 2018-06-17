import deck
import logic


# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.show_deck()
bj_deck.shuffle_deck()
bj_deck.show_deck()

# Create dealer and player one's hands
bj_deck.create_starting_hands()

# Draw cards for players
bj_deck.draw_card(player=True)
bj_deck.draw_card(dealer=True)

# Show hands
bj_deck.show_hand(player=True, dealer=True)

# Create logic object
game_logic = logic.create_logic(bj_deck)
game_logic.get_scores()

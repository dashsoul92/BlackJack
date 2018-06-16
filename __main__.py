import deck

# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.show_deck()
bj_deck.shuffle_deck()
bj_deck.show_deck()

# Create dealer and player one's hands
bj_deck.create_starting_hands()
bj_deck.draw_card(player=True)
bj_deck.draw_card(dealer=True)
bj_deck.show_hand(player=True, dealer=True)

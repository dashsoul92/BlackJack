import deck

# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.show_deck()
bj_deck.shuffle_deck()
bj_deck.show_deck()

# Create dealer and player one's hands
bj_deck.create_starting_hands(1)
bj_deck.show_hand(dealer=True)

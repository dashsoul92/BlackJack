import deck
import logic

# TODO Figure out the logic to dump the player and dealer's hands from the previous game into the graveyard
# TODO Handle multiple rounds rather than just the one round
# TODO Handle placing bets
# TODO Handle keeping track of bank

# Creating deck and shuffling it
bj_deck = deck.make_deck()
bj_deck.shuffle_deck()

# Create logic object
game_logic = logic.create_logic(bj_deck)

# Beginning the game
game_number = 0
game = True

while game:
    if game_number > 0:
        print(f"\nGame number: {game_number}")
        play_again = input("type 'y' to continue or 'n' to end the game: ")
        if play_again == 'y':
            game_number = game_logic.play_round(deck=bj_deck, logic=game_logic, game_number=game_number)
        elif play_again == 'n':
            game = False
    else:
        game_number = game_logic.play_round(deck=bj_deck, logic=game_logic, game_number=game_number)

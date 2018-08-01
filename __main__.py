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
game_number = 1

if game_number >= 1:
   print(f"\nGame number: {game_number}")
   while True:
       try:
           play_again = str(input("type 'y' to continue or 'n' to end the game: "))
           if play_again not in (['y','n']):
               raise ValueError
           break
       except ValueError:
           print: play_again + " is an invalid input."
   if play_again == 'y':
       game_number = game_logic.play_round(deck=bj_deck, logic=game_logic, game_number=game_number)
       print(f"The Graveyard consists of {bj_deck.graveyard}")
       print(f"The length of the dealer's deck is: {len(bj_deck.dealer_hand)}\n"
             f"The length of the player's deck is: {len(bj_deck.player_one_hand)}")
   elif play_again == 'n':
else:
   game_number = game_logic.play_round(deck=bj_deck, logic=game_logic, game_number=game_number)
   print(f"The Graveyard consists of {bj_deck.graveyard}")

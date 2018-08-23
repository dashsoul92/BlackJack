# BlackJack
**TODO**
- [Done] Create logic to handle bets
- [DONE] Create logic to handle splitting a hand (when the player or dealer draws two of the same card, for their starting hand)
- [DONE] Create logic for Insurance bet and update dealer hand reveal
- [DONE] Create logic for Double Down
- [DONE] Create logic for Surrender
- [DONE] Update logic to handle ace's multiple card values
- [DONE] Create logic to handle rounds
- [DONE] Create deck logic to reset deck once 46 cards have been drawn

Found bug: When graveyard was count = 33, game number = 28 got: 
  Message=IndexError('pop from empty list',)
  Source=c:\users\kevin_000\source\repos\blackjack\deck.py
  StackTrace:
  File "c:\users\kevin_000\source\repos\blackjack\deck.py", line 96, in draw_card
    dealer_card = self.deck.pop()
  File "c:\users\kevin_000\source\repos\blackjack\deck.py", line 78, in create_starting_hands
    self.draw_card(player=True, dealer=True)
  File "c:\users\kevin_000\source\repos\blackjack\logic.py", line 126, in play_round
    deck.create_starting_hands()
  File "c:\users\kevin_000\source\repos\blackjack\__main__.py", line 39, in <module>
    game_number, credits = game_logic.play_round(deck=bj_deck, logic=game_logic, game_number=game_number, credits=credits)
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\pydevd\_pydev_imps\_pydev_execfile.py", line 25, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\pydevd\pydevd.py", line 1035, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\pydevd\pydevd.py", line 1628, in main
    globals = debugger.run(setup['file'], None, None, is_module)
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\_main.py", line 101, in _run
    raise
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\_main.py", line 47, in run_file
    run(argv, addr, **kwargs)
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\packages\ptvsd\debugger.py", line 36, in debug
    run(address, filename, *args, **kwargs)
  File "c:\program files (x86)\microsoft visual studio\2017\enterprise\common7\ide\extensions\microsoft\python\core\ptvsd_launcher.py", line 111, in <module>
    vspd.debug(filename, port_num, debug_id, debug_options, run_as)



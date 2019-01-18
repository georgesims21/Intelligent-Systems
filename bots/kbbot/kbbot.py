#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State, util, Deck
import random
from . import load
from .kb import KB, Boolean, Integer

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()
        chosen_move = moves[0]
        moves_trump_suit = []

        random.shuffle(moves)

        # ----------------------------------- #
        # If it's our turn, play a trump if possible, else we should
        # play the highest card in the available moves

        # If the opponent hasn't played a card
        if state.get_opponents_played_card() is None:
            
            print("WE PLAY FIRST")

            #Get all trump suit moves available
            for index, move in enumerate(moves):
                
                if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                    moves_trump_suit.append(move)

            # Return if a trump
            if len(moves_trump_suit) > 0:
                return moves_trump_suit[0]
        
        # Get move with highest rank available, of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    chosen_move = move
            
            return chosen_move

        # ----------------------------------- #
        # Else our bot plays a strategy

        # Aces first
        else:
            for move in moves:

                if not self.aces_consistent(state, move):
                    # Plays the first move that makes the kb inconsistent. We do not take
                    # into account that there might be other valid moves according to the strategy.
                    # Uncomment the next line if you want to see that something happens.
                    print ("ACE Strategy Applied")
                    return move
            # No aces then jacks
            for move in moves:

                if not self.jacks_consistent(state, move):
                    # Plays the first move that makes the kb inconsistent. We do not take
                    # into account that there might be other valid moves according to the strategy.
                    # Uncomment the next line if you want to see that something happens.
                    print ("JACK Strategy Applied")
                    return move

            # If no move that is entailed by the kb is found, play random move
            print ("Strategy Not Applied")
            return random.choice(moves)

    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def jacks_consistent(self, state, move):
    # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        jkb = KB()

        # Add general information about the game
        load.jacks_information(jkb)

        # Add the necessary knowledge about the strategy
        load.jacks_knowledge(jkb)

        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]
        
        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if 
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        jkb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)

        return jkb.satisfiable()

    def aces_consistent(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        akb = KB()

        # Add general information about the game
        load.aces_information(akb)

        # Add the necessary knowledge about the strategy
        load.aces_knowledge(akb)

        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if 
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pa" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        akb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)

        return akb.satisfiable()

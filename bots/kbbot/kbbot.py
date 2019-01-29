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

played_cards = []

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()
        chosen_move = moves[0]
        moves_trump_suit = []

        random.shuffle(moves)

        # --------------- implement probability here ---------------- #

        # 20 cards in total, 1 is overturned for the trump in phase 1. 5 in each players hand. 5 of the total are trump cards

                #      	    Aces 	10s 	Kings 	Queens 	Jacks
        # Clubs 	    0 	    1 	    2 	    3 	    4
        # Diamonds 	    5 	    6 	    7 	    8 	    9
        # Hearts 	    10 	    11 	    12 	    13 	    14
        # Spades 	    15 	    16 	    17 	    18 	    19

        # state = State.generate()
        # To deterministically generate the same state each time, the generate method can also take a seed, like so:
        # print("TEST STATE:")
        # state = State.generate(1)
        # This will always generate the same starting state, to make testing/debugging your bots easier.
        # Note that any two states generated with the same seed will be identical, and 25 is only used here as an example.
        # print(state) #-- formats the same as each trick when playing play.py against two bots

        # to extract points from certain player
        # me = state.whose_turn()
        # opponent = util.other(me)
        # own_points = state.get_points(me)
        # opponents_points = state.get_points(opponent)

        # State.make_assumption()
		# Takes the current imperfect information state and makes a 
		# random guess as to the states of the unknown cards.
		# :return: A perfect information state object.

        size_of_stock = state.get_stock_size() # int, max 10 min 0 in phase 2

        total_aces_in_deck = 4
        total_tens_in_deck = 4
        total_kings_in_deck = 4
        total_queens_in_deck = 4
        total_jacks_in_deck = 4
        my_aces = 0

        if state.get_prev_trick() != [None, None]:
            card1, card2 = state.get_prev_trick()
            played_cards.append(card1)
            played_cards.append(card2)
        
        for index in played_cards:
            if index % 5 == 0:
                played_aces = played_aces + 1

        hand = state.hand()

        # Negate hand cards from possibilities
        for index in hand:
            if index % 5 == 0:
                my_aces = my_aces + 1
                total_aces_in_deck = total_aces_in_deck - 1 
                
            elif index % 5 == 1:
                total_tens_in_deck = total_tens_in_deck - 1
            elif index % 5 == 2:
                total_kings_in_deck = total_kings_in_deck - 1
            elif index % 5 == 3:
                total_queens_in_deck = total_queens_in_deck - 1
            elif index % 5 == 4:
                total_jacks_in_deck = total_jacks_in_deck - 1
        
        secret_formula = 1 - (((size_of_stock + my_aces) / 5) / (20 / 5))
        # secret_formula = ((my_aces + played_aces) / size_of_stock + 5)

        # print("FORMULA = ", secret_formula)

        if my_aces > 0:
            print("I HAVE AN ACE")
            


            
            
            



        





        # --------------- implement probability here ---------------- #

        # If the opponent hasn't played a card
        if state.get_opponents_played_card() is None:
            
            '''
            TODO: 
            Extract already played cards info
            Extract cards in hand info*
            Extract how many cards are left in the deck*
            Calculate the chance of certain card being played based on this info

            '''

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

        # Else our bot plays a strategy
        else:

            '''
            TODO:   Implement the play trump tactic if we don't have a legible card to play
                    Optimize cheap strategy to play lowest card first
            '''

            # Is our best card worse than the opponents played card?
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    chosen_move = move
            
            if chosen_move[0] % 5 > state.get_opponents_played_card() % 5:
                # Play our cheapest card if we can't beat it. Less than (<) due to if less than equal (<=) card is
                # not legible.. unless trump card
                for move in moves:
                    if not self.cheap_consistent(state, move):
                        #print ("CHEAP Strategy Applied")
                        return move
            else:
                # Aces first
                for move in moves:
                    if not self.aces_consistent(state, move):
                        #print ("ACE Strategy Applied")
                        return move

                # No aces then jacks
                for move in moves:
                    if not self.jacks_consistent(state, move):
                        #print ("JACK Strategy Applied")
                        return move

            # If no move that is entailed by the kb is found, play random move
            #print ("Strategy Not Applied")
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
        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        jkb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)

        return jkb.satisfiable()

    def aces_consistent(self, state, move):
        akb = KB()

        load.aces_information(akb)
        load.aces_knowledge(akb)
        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        akb.add_clause(~strategy_variable)

        return akb.satisfiable()

    def cheap_consistent(self, state, move):
        kb = KB()

        load.cheap_information(kb)
        load.cheap_knowledge(kb)
        index = move[0]

        variable_string = "p" + str(index)
        strategy_variable = Boolean(variable_string)

        kb.add_clause(~strategy_variable)

        return kb.satisfiable()

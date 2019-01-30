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
from scipy.stats import hypergeom

import numpy as np

played_cards = []


class Bot:

    def __init__(self):
        pass

    def nb_played(self,state,cardRank):
        played_or_in_hand = 0
        my_hand = state.hand()
        for index in my_hand:
            if util.get_rank(index)== cardRank:
                played_or_in_hand = played_or_in_hand + 1

        trickplayed = state.get_all_tricks()
        for index in trickplayed:
            if util.get_rank(index)== cardRank:
                played_or_in_hand = played_or_in_hand + 1
        return played_or_in_hand

    def nb_trump(self,state):
        played_or_in_hand = 0
        my_hand = state.hand()
        for index in my_hand:
            if util.get_suit(index) == state.get_trump_suit():
                played_or_in_hand = played_or_in_hand + 1

        trickplayed = state.get_all_tricks()
        for index in trickplayed:
            if util.get_suit(index) == state.get_trump_suit():
                played_or_in_hand = played_or_in_hand + 1
        return played_or_in_hand

    def hypergeometric(self,played_or_in_hand,total_success,state):

        stock = state.get_stock_size() + 5
        if played_or_in_hand == total_success:
            prob = 0
        else:      
            secret_formula = hypergeom(stock , total_success-(played_or_in_hand), 5)
            arange = np.arange(0, 4)
            notAce = secret_formula.pmf(arange)
            prob = 1 - notAce[0]
        return prob
    
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

        aces = self.nb_played(state,"A")
        tens = self.nb_played(state,"10")
        kings = self.nb_played(state,"K")
        queens = self.nb_played(state,"Q")
        jacks = self.nb_played(state,"J")
        nb_trump_played = self.nb_trump(state)


        probAces = self.hypergeometric(aces,4,state)
        probTens = self.hypergeometric(tens,4,state)
        probKings = self.hypergeometric(kings,4,state)
        probQueens = self.hypergeometric(queens,4,state)
        probJacks = self.hypergeometric(jacks,4,state)
        probTrumps = self.hypergeometric(nb_trump_played,5,state)

        if state.get_opponents_played_card() is None:   
            '''
            TODO: 
            Extract already played cards info
            Extract cards in hand info*
            Extract how many cards are left in the deck*
            Calculate the chance of certain card being played based on this info

            '''
            for index, move in enumerate(moves):     
                if probTrumps < 0.3:
                    for move in moves:
                        if not self.aces_consistent(state, move):
                            #print ("ACE Strategy Applied")
                            return move
                elif probTrumps > 0.6
                    for move in moves:
                        if not self.cheap_consistent(state, move):
                            #print ("CHEAP Strategy Applied")
                            return move
                elif probTrumps > 0.6
                    for move in moves:
                        if not self.cheap_consistent(state, move):
                            #print ("CHEAP Strategy Applied")
                            return move
                        


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

    def kings_consistent(self, state, move):
    akb = KB()

    load.kings_information(akb)
    load.kings_knowledge(akb)
    index = move[0]

    variable_string = "p" + str(index)
    strategy_variable = Boolean(variable_string)

    akb.add_clause(~strategy_variable)

    return akb.satisfiable()

    def queens_consistent(self, state, move):
    akb = KB()

    load.queens_information(akb)
    load.queens_knowledge(akb)
    index = move[0]

    variable_string = "p" + str(index)
    strategy_variable = Boolean(variable_string)

    akb.add_clause(~strategy_variable)

    return akb.satisfiable()

    def tens_consistent(self, state, move):
    akb = KB()

    load.tens_information(akb)
    load.tens_knowledge(akb)
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

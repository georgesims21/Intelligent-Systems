from .kb import KB, Boolean, Integer

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.

# --- jacks --- #
J4 = Boolean('j4')
J9 = Boolean('j9')
J14 = Boolean('j14')
J19 = Boolean('j19')

# --- queen --- #
Q3 = Boolean('q3')
Q8 = Boolean('q8')
Q13 = Boolean('q13')
Q18 = Boolean('q18')

# --- kings --- #
K2 = Boolean('k2')
K7 = Boolean('k7')
K12 = Boolean('k12')
K17 = Boolean('k17')

# --- tens --- #
T1 = Boolean('t1')
T6 = Boolean('t6')
T11 = Boolean('t11')
T16 = Boolean('t16')

# --- aces --- #
A0 = Boolean('a0')
A5 = Boolean('a5')
A10 = Boolean('a10')
A15 = Boolean('a15')

P0 = Boolean('p0')
P1 = Boolean('p1')
P2 = Boolean('p2')
P3 = Boolean('p3')
P4 = Boolean('p4')
P5 = Boolean('p5')
P6 = Boolean('p6')
P7 = Boolean('p7')
P8 = Boolean('p8')
P9 = Boolean('p9')
P10 = Boolean('p10')
P11 = Boolean('p11')
P12 = Boolean('p12')
P13 = Boolean('p13')
P14 = Boolean('p14')
P15 = Boolean('p15')
P16 = Boolean('p16')
P17 = Boolean('p17')
P18 = Boolean('p18')
P19 = Boolean('p19')


def jacks_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)
    # Add here whatever is needed for your strategy.

def jacks_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Add clauses (This list is sufficient for this strategy)
    # PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
    # In other words that the PJ strategy should play a card when it is a jack
    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)
    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

def aces_information(kb):
    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)

def aces_knowledge(kb):
    # Play an ace
    kb.add_clause(~A0, P0)
    kb.add_clause(~A5, P5)
    kb.add_clause(~A10, P10)
    kb.add_clause(~A15, P15)
    kb.add_clause(~P0, A0)
    kb.add_clause(~P5, A5)
    kb.add_clause(~P10, A10)
    kb.add_clause(~P15, A15)

def cheap_information(kb):
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

def cheap_knowledge(kb):
    # Play a cheap card (J < Q < K)

    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)
    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

    kb.add_clause(~Q3, P3)
    kb.add_clause(~Q8, P8)
    kb.add_clause(~Q13, P13)
    kb.add_clause(~Q18, P18)
    kb.add_clause(~P3, Q3)
    kb.add_clause(~P8, Q8)
    kb.add_clause(~P13, Q13)
    kb.add_clause(~P18, Q18)

    kb.add_clause(~K2, P2)
    kb.add_clause(~K7, P7)
    kb.add_clause(~K12, P12)
    kb.add_clause(~K17, P17)
    kb.add_clause(~P2, K2)
    kb.add_clause(~P7, K7)
    kb.add_clause(~P12, K12)
    kb.add_clause(~P17, K17)


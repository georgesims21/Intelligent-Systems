import sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.

'''
TODO:   *Change all J0, ... , J19 to their actual values according to github
        *Change all PJ0, ... , PJ19 to their actual values ///
'''
AC = Boolean('a0')
TC = Boolean('t1')
KC = Boolean('k2')
QC = Boolean('q3')
JC = Boolean('j4')
AD = Boolean('a5')
TD = Boolean('t6')
KD = Boolean('k7')
QD = Boolean('q8')
JD = Boolean('j9')
AH = Boolean('a10')
TH = Boolean('t11')
KH = Boolean('k12')
QH = Boolean('q13')
JH = Boolean('j14')
AS = Boolean('a15')
TS = Boolean('t16')
KS = Boolean('k17')
QS = Boolean('q18')
JS = Boolean('j19')

PAC = Boolean('pa0')
PTC = Boolean('pt1')
PKC = Boolean('pk2')
PQC = Boolean('pq3')
PJC = Boolean('pj4')
PAD = Boolean('pa5')
PTD = Boolean('pt6')
PKD = Boolean('pk7')
PQD = Boolean('pq8')
PJD = Boolean('pj9')
PAH = Boolean('pa10')
PTH = Boolean('pt11')
PKH = Boolean('pk12')
PQH = Boolean('pq13')
PJH = Boolean('pj14')
PAS = Boolean('pa15')
PTS = Boolean('pt16')
PKS = Boolean('pk17')
PQS = Boolean('pq18')
PJS = Boolean('pj19')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are Jacks
kb.add_clause(JC)
kb.add_clause(JD)
kb.add_clause(JH)
kb.add_clause(JS)
# Add here whatever is needed for your strategy.

# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
# In other words that the PJ strategy should play a card when it is a jack
kb.add_clause(~JC, PJC)
kb.add_clause(~JD, PJD)
kb.add_clause(~JH, PJH)
kb.add_clause(~JS, PJS)
kb.add_clause(~PJC, JC)
kb.add_clause(~PJD, JD)
kb.add_clause(~PJH, JH)
kb.add_clause(~PJS, JS)
# Add here other strategies

kb.add_clause(~JC)
# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())
